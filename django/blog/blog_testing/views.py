# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from post.models import Post


def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(
        request, 'home.html', context=context, content_type='text/html')
    # first_post_content = Post.objects.first().content
    # return HttpResponse(first_post_content)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return HttpResponse(post.content)


def login_(request):
    if request.user.is_authenticated:
        return redirect(reverse('homepage'))
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('homepage'))
        else:
            context['error'] = 'Invalid Username or Password'
            context['username'] = username
    return render(request, 'login_.html', context=context)


def logout_(request):
    logout(request)
    return redirect(reverse('login'))
