from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_home, name="tweet_home"),
    path('view', views.get_tweets, name="get_tweets"),
    path('save', views.save_tweets, name="save_tweets"),
    path('edit/{tweet_id}', views.tweet_edit, name="tweet_edit"),
    path('delete/{tweet_id}', views.tweet_delete, name="tweet_delete"),
]