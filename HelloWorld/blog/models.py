# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Artical (models.Model):
     title = models.CharField(max_length=32,default='title')
     content = models.TextField(null=True)
# Create your models here.
