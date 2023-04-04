from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path(r'^(?P<pk>[0-9]+)/$', views.NewsDetailView.as_view(), name='news-detail'),
    path(r'^(?P<pk>[0-9]+)/$/update', views.NewsUpdateView.as_view(), name='news-update'),
    path(r'^(?P<pk>[0-9]+)/$/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]
