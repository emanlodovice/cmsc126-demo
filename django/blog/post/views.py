# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .models import Post


def homepage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'home__.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return HttpResponse(post.content)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            context['error_message'] = 'wrong username or password'
            context['username'] = username
    return render(request, 'home/login.html', context=context)
