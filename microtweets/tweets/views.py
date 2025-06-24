from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets.html',{'tweets':tweets})

def save_tweets(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('get_tweets')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form':form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "PUT":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('get_tweets')
    else:
        form = TweetForm(instance= tweet)
    return render(request, 'tweet_form.html', {'form': form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "DELETE":
        tweet.is_deleted = True
        tweet.save()
    return redirect('get_tweets')