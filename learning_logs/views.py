'''
Author: Rober Chou
Date: 2020-10-16 14:30:18
LastEditTime: 2020-11-16 13:49:45
LastEditors: Rober Chou
Description: 
symbol_custom_string_obkoro1: Code make our world better！！
'''

from django.urls import reverse
from django.http.response import HttpResponseRedirect
from learning_logs.forms import EntryForm, TopicForm
from django.http import request
from django.shortcuts import render
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    # topics = Topic.objects.order_by("date_added")
    topic = Topic.objects.get(id=topic_id)
    #根据请求确认属于哪个用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(
                reverse('learning_logs:topic', args=[topic_id]))
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
