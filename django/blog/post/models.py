# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='posts')
    content = models.TextField()
    likes_counter = models.IntegerField(default=0)
    when_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content
