# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import adminViews

urlpatterns = [

    #  定义添加管理员的url地址响应方法，跳转到 adminView的addadmin方法
    url(r'^addadmin/$', adminViews.addadmin, name='addadmin'),

    #  定义处理添加管理员的url地址响应方法，跳转到 adminView的addadminact方法
    url(r'^addadminact/$', adminViews.addadminact, name='addadminact'),

    #  定义跳转修改管理员的url地址响应方法，跳转到 adminView的updateadmin方法
    url(r'^updateadmin/(?P<id>[0-9]+)$', adminViews.updateadmin, name='updateadmin'),

    #  定义处理修改管理员的url地址响应方法，跳转到 adminView的updateadminat方法
    url(r'^updateadminact/$', adminViews.updateadminact, name='updateadminact'),

    #  定义跳转管理管理员的url地址响应方法，跳转到 adminView的adminmanage方法
    url(r'^adminmanage/$', adminViews.adminmanage, name='adminmanage'),

    #  定义跳转查看管理员的url地址响应方法，跳转到 adminView的adminview方法
    url(r'^adminview/$', adminViews.adminview, name='adminview'),

    #  定义处理删除管理员的url地址响应方法，跳转到 adminView的deleteadmin方法
    url(r'^deleteadminact/(?P<id>[0-9]+)$', adminViews.deleteadminact, name='deleteadminact'),

    #  定义跳转搜索管理员的url地址响应方法，跳转到 adminView的searchadmin方法
    url(r'^searchadmin/$', adminViews.searchadmin, name='searchadmin'),

    #  定义管理员详情的url地址响应方法，跳转到 adminView的admindetails方法
    url(r'^admindetails/(?P<id>[0-9]+)$', adminViews.admindetails, name='admindetails'),
]
