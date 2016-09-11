# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from photoblog.views.view_articles import articles

urlpatterns = [
    url(r'^articles/', articles),
]
