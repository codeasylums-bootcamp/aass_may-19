import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import facebook
from .forms import *

# Create your views here.
from core.models import FacebookStatus


@login_required
def home(request):
    return render(request, 'index.html')


def privacy(request):
    return render(request, 'privacy.html')


@login_required
def add_post(request):
    if request.method == 'POST':
        form = UserPostSubmit(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = UserPostSubmit()
    return render(request, 'post_submit.html', {'form': form})


@login_required
def publish(request):
    user = request.user
    messages = FacebookStatus.objects.filter(status='approved', publish_timestamp=None, author=user)[:1]
    if not messages:
        x = 'There are no pending messages for %s' % user
        return render(request, 'publish.html', {'x':x})
    message = messages[0]
    auth = user.social_auth.first()
    if not auth:
        x = 'User %s is not authenticated with Facebook' % user
        return render(request, 'publish.html', {'x': x})
    graph = facebook.GraphAPI(auth.extra_data['access_token'])
    graph.put_object("me", "feed", message=message.message)
    message.publish_timestamp = datetime.datetime.now()
    message.save()
    x = 'all good'
    return render(request, 'publish.html', {'x': x})
