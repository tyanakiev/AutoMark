from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'index.html'}),
    url(r'^automark/twitter', views.twitter, name='twitter'),
    url(r'^automark/facebook', views.facebook, name='facebook'),
    url(r'^automark/instagram_settings/(?P<pk>\d+)/$', views.instagram_settings, name='instagram_settings'),
    url(r'^automark/instagram_report/(?P<pk>\d+)/$', views.instagram_report, name='instagram_report'),
    url(r'^automark/i_worker_start/(?P<pk>\d+)/$', views.i_worker_start, name='i_worker_start'),
    url(r'^automark/delete_insta_acc/(?P<pk>\d+)/$', views.delete_insta_acc, name='delete_insta_acc'),
    url(r'^automark/instagram', views.instagram, name='instagram'),
    url(r'^automark/statistics', views.stats, name='stats'),
    url(r'^register/', views.register),
    url(r'^user_profile/', views.user_profile, name='user_profile'),

]
# delete_insta_acc