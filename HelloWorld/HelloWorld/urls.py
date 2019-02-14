from django.conf.urls import url,include
from django.contrib import admin
from . import view

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^index/',include(blog.urls))
]
