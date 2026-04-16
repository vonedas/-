# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import yaoViews

urlpatterns = [

    #  定义添加吃药提醒的url地址响应方法，跳转到 yaoView的addyao方法
    url(r'^addyao/$', yaoViews.addyao, name='addyao'),

    #  定义处理添加吃药提醒的url地址响应方法，跳转到 yaoView的addyaoact方法
    url(r'^addyaoact/$', yaoViews.addyaoact, name='addyaoact'),

    #  定义跳转修改吃药提醒的url地址响应方法，跳转到 yaoView的updateyao方法
    url(r'^updateyao/(?P<id>[0-9]+)$', yaoViews.updateyao, name='updateyao'),

    #  定义处理修改吃药提醒的url地址响应方法，跳转到 yaoView的updateyaoat方法
    url(r'^updateyaoact/$', yaoViews.updateyaoact, name='updateyaoact'),

    #  定义跳转管理吃药提醒的url地址响应方法，跳转到 yaoView的yaomanage方法
    url(r'^yaomanage/$', yaoViews.yaomanage, name='yaomanage'),

    #  定义跳转查看吃药提醒的url地址响应方法，跳转到 yaoView的yaoview方法
    url(r'^yaoview/$', yaoViews.yaoview, name='yaoview'),

    #  定义处理删除吃药提醒的url地址响应方法，跳转到 yaoView的deleteyao方法
    url(r'^deleteyaoact/(?P<id>[0-9]+)$', yaoViews.deleteyaoact, name='deleteyaoact'),

    #  定义跳转搜索吃药提醒的url地址响应方法，跳转到 yaoView的searchyao方法
    url(r'^searchyao/$', yaoViews.searchyao, name='searchyao'),

    #  定义吃药提醒详情的url地址响应方法，跳转到 yaoView的yaodetails方法
    url(r'^yaodetails/(?P<id>[0-9]+)$', yaoViews.yaodetails, name='yaodetails'),
]
