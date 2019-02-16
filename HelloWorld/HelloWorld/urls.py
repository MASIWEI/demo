from django.conf.urls import url, include
from . import view
import blog.views as bv

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^blog/', bv.index),
]
