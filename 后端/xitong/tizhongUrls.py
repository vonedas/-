# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import tizhongViews

urlpatterns = [

    #  定义添加体重的url地址响应方法，跳转到 tizhongView的addtizhong方法
    url(r'^addtizhong/$', tizhongViews.addtizhong, name='addtizhong'),

    #  定义处理添加体重的url地址响应方法，跳转到 tizhongView的addtizhongact方法
    url(r'^addtizhongact/$', tizhongViews.addtizhongact, name='addtizhongact'),

    #  定义跳转修改体重的url地址响应方法，跳转到 tizhongView的updatetizhong方法
    url(r'^updatetizhong/(?P<id>[0-9]+)$', tizhongViews.updatetizhong, name='updatetizhong'),

    #  定义处理修改体重的url地址响应方法，跳转到 tizhongView的updatetizhongat方法
    url(r'^updatetizhongact/$', tizhongViews.updatetizhongact, name='updatetizhongact'),

    #  定义跳转管理体重的url地址响应方法，跳转到 tizhongView的tizhongmanage方法
    url(r'^tizhongmanage/$', tizhongViews.tizhongmanage, name='tizhongmanage'),

    #  定义跳转查看体重的url地址响应方法，跳转到 tizhongView的tizhongview方法
    url(r'^tizhongview/$', tizhongViews.tizhongview, name='tizhongview'),

    #  定义处理删除体重的url地址响应方法，跳转到 tizhongView的deletetizhong方法
    url(r'^deletetizhongact/(?P<id>[0-9]+)$', tizhongViews.deletetizhongact, name='deletetizhongact'),

    #  定义跳转搜索体重的url地址响应方法，跳转到 tizhongView的searchtizhong方法
    url(r'^searchtizhong/$', tizhongViews.searchtizhong, name='searchtizhong'),

    #  定义体重详情的url地址响应方法，跳转到 tizhongView的tizhongdetails方法
    url(r'^tizhongdetails/(?P<id>[0-9]+)$', tizhongViews.tizhongdetails, name='tizhongdetails'),

    #  定义添加体重方法，响应页面请求，跳转到tizhongViews的useraddtizhong方法
    url(r'^useraddtizhong/$', tizhongViews.useraddtizhong, name='useraddtizhong'),

    #  定义处理添加体重方法，响应页面请求，跳转到tizhongViews的useraddtizhongact方法
    url(r'^useraddtizhongact/$', tizhongViews.useraddtizhongact, name='useraddtizhongact'),

    #  定义跳转修改体重方法，响应页面请求，跳转到tizhongViews的userupdatetizhong方法
    url(r'^userupdatetizhong/(?P<id>[0-9]+)$', tizhongViews.userupdatetizhong, name='userupdatetizhong'),

    #  定义处理修改体重方法，响应页面请求，跳转到tizhongViews的userupdatetizhongact方法
    url(r'^userupdatetizhongact/$', tizhongViews.userupdatetizhongact, name='userupdatetizhongact'),

    #  定义跳转体重管理方法，响应页面请求，跳转到tizhongViews的usertizhongmanage方法
    url(r'^usertizhongmanage/$', tizhongViews.usertizhongmanage, name='usertizhongmanage'),

    #  定义处理删除体重方法，响应页面请求，跳转到tizhongViews的userdeletetizhong方法
    url(r'^userdeletetizhongact/(?P<id>[0-9]+)$', tizhongViews.userdeletetizhongact, name='userdeletetizhongact'),
]
