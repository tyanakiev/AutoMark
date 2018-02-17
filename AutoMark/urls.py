from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'index.html'}),
    url(r'^automark/twitter', views.twitter, name='twitter'),
    url(r'^automark/facebook', views.facebook, name='facebook'),
    url(r'^automark/instagram', views.instagram, name='instagram'),
    url(r'^automark/statistics', views.stats, name='stats'),
    url(r'^register/', views.register),
]