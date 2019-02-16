# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from . import models
def index(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index.html' ,{article:"article"})





# Create your views here.
