# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def homepage(request):
    return render(request, 'home/homepage.html')
