# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        verbose_name=u'Статья'
        verbose_name_plural=u'Статьи'

    title = models.CharField(max_length=64)
    text = models.TextField()
    image = models.ImageField(blank=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    #user = models.ForeignKey('User')

    def __unicode__(self):
        return u'%s' % (self.title)
