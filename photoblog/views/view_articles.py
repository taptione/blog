# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from photoblog.models.article import Article

def articles(request):
    return render(request, 'articles.html', {'artcl':Article.objects.all()})