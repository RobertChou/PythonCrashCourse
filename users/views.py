'''
Author: Rober Chou
Date: 2020-11-05 22:28:44
LastEditTime: 2020-11-12 09:51:20
LastEditors: Rober Chou
Description: 
symbol_custom_string_obkoro1: Code make our world better！！
'''
from django.shortcuts import render
from django.http import request
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
