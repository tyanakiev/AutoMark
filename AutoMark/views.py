from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm, InstagramSettingsForm
from AutoMark.models import InstagramAccount, InstagramSettings


# Create your views here.

def twitter(request):
    return render(request, 'twitter.html')


def facebook(request):
    return render(request, 'facebook.html')


def instagram_settings(request):
    if request.method == 'POST':
        form = InstagramSettingsForm(request.POST)
        if form.is_valid():
            user_obj = form.cleaned_data
            print(user_obj)
            new_account = InstagramSettings(
                user_obj['tags'],
                user_obj['locations'],
                user_obj['likes_hour'],
                user_obj['comments_hour'],
                user_obj['follows_hour'],
                user_obj['unfollows_hour'],
                user_obj['posted'],
                user_obj['comments']
            )
            new_account.save()
    else:
        form = InstagramSettingsForm()
    return render(request, 'instagram/insta_settings.html', {'form': form})


def instagram(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            new_account = InstagramAccount(username=userObj['username'])
            new_account.save()
    all_instagram_accounts = InstagramAccount.objects.all()
    return render(request, 'instagram.html', {'accounts': all_instagram_accounts})


def stats(request):
    return render(request, 'stats.html')


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
                User.objects.create_user(username, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
