from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('view', views.get_tweets),
    path('save', views.save_tweets),
    path('edit/{tweet_id}', views.tweet_edit),
    path('delete/{tweet_id}', views.tweet_delete),
]