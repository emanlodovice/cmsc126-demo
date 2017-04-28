# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from post.models import Post


def homepage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(
        request, 'home.html', context=context, content_type='text/html')
    # first_post_content = Post.objects.first().content
    # return HttpResponse(first_post_content)
