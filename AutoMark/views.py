import os

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, InstagramSettingsForm, InstagramAccountForm
from AutoMark.models import InstagramAccount, InstagramSettings, InstagramCeleryTask
from AutoMark.Celery.tasks import insta_py
from celery.task.control import revoke
from django.core.exceptions import ObjectDoesNotExist


def twitter(request):
    return render(request, 'twitter.html')


def facebook(request):
    return render(request, 'facebook.html')


def user_profile(request):
    return render(request, 'user_profile.html')


def instagram_settings(request, pk=None):
    saved_settings = None
    current_task = None
    if request.method == 'POST':
        form = InstagramSettingsForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data
            print(user_obj)
            new_account = InstagramSettings(
                pk,
                user_obj['tags'],
                user_obj['locations'],
                user_obj['likes_hour'],
                user_obj['comments_hour'],
                user_obj['follows_hour'],
                user_obj['unfollows_hour'],
                user_obj['comments']
            )
            new_account.save()
    else:
        form = InstagramSettingsForm()
        try:
            saved_settings = InstagramSettings.objects.get(id=pk)
            current_task = InstagramCeleryTask.objects.get(pk=pk)
            form = InstagramSettingsForm({'tags': saved_settings.tags,
                                          'locations': saved_settings.locations,
                                          'likes_hour': saved_settings.likes_hour,
                                          'comments_hour': saved_settings.comments_hour,
                                          'follows_hour': saved_settings.follows_hour,
                                          'unfollows_hour': saved_settings.unfollows_hour,
                                          'comments': saved_settings.comments})
        except:
            print("There are no settings with that id: ", pk)
    return render(request, 'insta_settings.html', {'form': form, 'id': pk,
                                                   'saved_settings': saved_settings,
                                                   'task': current_task})


def i_worker_start(request, pk=None):
    i_account = InstagramAccount.objects.get(pk=pk)
    current_settings = InstagramSettings.objects.get(id=pk)
    insta_settings = {'username': i_account.username,
                      'password': i_account.password,
                      'tags': current_settings.tags.split(','),  # ['liverpool', 'lpfc', 'Liverpool Football'],
                      'locations': current_settings.locations,
                      'likes_hour': int(current_settings.likes_hour),
                      'comments_hour': int(current_settings.comments_hour),
                      'follows_hour': int(current_settings.follows_hour),
                      'unfollows_hour': int(current_settings.unfollows_hour),
                      'comments': current_settings.comments.split(',')  # ['Wow', 'Amazing', 'Super!', 'This looks amazing.']}
                      }
    insta_py.delay(insta_settings, pk)
    return redirect('instagram')


def i_worker_stop(request, pk=None):
    current_task = InstagramCeleryTask.objects.get(pk=pk)
    revoke(current_task.task_id, terminate=True)
    current_task.status = 'Stopped'
    current_task.save()
    return redirect('instagram')


def instagram(request):
    if request.method == 'POST':
        form = InstagramAccountForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            new_account = InstagramAccount(username=userObj['username'], password=userObj['password'],
                                           created_by=request.user)
            new_account.save()
    all_instagram_accounts = InstagramAccount.objects.all()
    form = InstagramAccountForm()
    return render(request, 'instagram.html', {'accounts': all_instagram_accounts, 'form': form})


def delete_insta_acc(request, pk=None):
    if request.is_ajax() and request.method == 'POST':
        i_account = InstagramAccount.objects.get(pk=pk)
        i_account.delete()
        try:
            current_task = InstagramCeleryTask.objects.get(pk=pk)
            current_task.delete()
            i_worker_stop(request, pk)
        except:
            print("Stopping task and deleting it.")
        try:
            saved_settings = InstagramSettings.objects.get(id=pk)
            saved_settings.delete()
        except ObjectDoesNotExist as err:
            print(err)
    all_instagram_accounts = InstagramAccount.objects.all()
    form = InstagramAccountForm()
    return render(request, 'instagram.html', {'accounts': all_instagram_accounts, 'form': form})


def stats(request):
    return render(request, 'stats.html')


def read_instagram_log_file(path):
    if os.path.exists(path):
        with open(path) as fhl:
            return fhl.readlines()
    return ['No log']


def instagram_report(request, pk=None):
    instagram_account = InstagramAccount.objects.get(id=pk)
    log_file_path = os.path.join('logs', instagram_account.username, 'general.log')
    content = read_instagram_log_file(log_file_path)
    return render(request, 'insta_report.html', {'account': instagram_account,
                                                 'content': content})


def automark(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists()):
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
