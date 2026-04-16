from django.conf.urls import url
from django.contrib import admin
from . import indexViews

urlpatterns = [
    url(r'^index/$', indexViews.index, name='index'),
    url(r'^indexjson/$', indexViews.indexjson, name='indexjson'),
]
