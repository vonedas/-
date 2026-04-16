# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import noticeViews

urlpatterns = [

    #  定义添加公告的url地址响应方法，跳转到 noticeView的addnotice方法
    url(r'^addnotice/$', noticeViews.addnotice, name='addnotice'),

    #  定义处理添加公告的url地址响应方法，跳转到 noticeView的addnoticeact方法
    url(r'^addnoticeact/$', noticeViews.addnoticeact, name='addnoticeact'),

    #  定义跳转修改公告的url地址响应方法，跳转到 noticeView的updatenotice方法
    url(r'^updatenotice/(?P<id>[0-9]+)$', noticeViews.updatenotice, name='updatenotice'),

    #  定义处理修改公告的url地址响应方法，跳转到 noticeView的updatenoticeat方法
    url(r'^updatenoticeact/$', noticeViews.updatenoticeact, name='updatenoticeact'),

    #  定义跳转管理公告的url地址响应方法，跳转到 noticeView的noticemanage方法
    url(r'^noticemanage/$', noticeViews.noticemanage, name='noticemanage'),

    #  定义跳转查看公告的url地址响应方法，跳转到 noticeView的noticeview方法
    url(r'^noticeview/$', noticeViews.noticeview, name='noticeview'),

    #  定义处理删除公告的url地址响应方法，跳转到 noticeView的deletenotice方法
    url(r'^deletenoticeact/(?P<id>[0-9]+)$', noticeViews.deletenoticeact, name='deletenoticeact'),

    #  定义跳转搜索公告的url地址响应方法，跳转到 noticeView的searchnotice方法
    url(r'^searchnotice/$', noticeViews.searchnotice, name='searchnotice'),

    #  定义公告详情的url地址响应方法，跳转到 noticeView的noticedetails方法
    url(r'^noticedetails/(?P<id>[0-9]+)$', noticeViews.noticedetails, name='noticedetails'),
]
