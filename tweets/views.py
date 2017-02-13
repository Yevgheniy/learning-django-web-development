# coding= UTF-8
from django.views.generic import View
from django.shortcuts import render
from user_profile.models import User
from models import Tweet
from tweets.forms import TweetForm


class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Django"
        return render(request, 'base.html', params)


class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()
        user = User.objects.get (username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)


class PostTweet(View):
    """Tweet Post form available on page /user/<username> URL"""
    def post(self, request, username):
        form = TweetForm(self.request.POST)
        if form.is_valid():
            user = User.objects.get(username=username)
            tweet = Tweet(text=form.cleaned_data['text'],
                                         user=user,
                                         country=form.cleaned_data['country'])
            tweet.save()
            words = form.cleaned_data['text'].split(" ")
            for word in words:
                if word[0] == "#":
                    HashTag, created = HashTag.objects.get_or_create(name=word[1:])
                    HashTag.tweet.add(tweet)
        return HttpResponseRedirect('/user/'+username)

