from django.conf.urls import url, include
from django.contrib import admin
from . import view
import blog.views as bv

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$', view.hello),
    url(r'^blog/', bv.index),
]
