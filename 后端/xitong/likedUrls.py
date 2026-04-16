# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import likedViews

urlpatterns = [

    #  定义添加点赞的url地址响应方法，跳转到 likedView的addliked方法
    url(r'^addliked/$', likedViews.addliked, name='addliked'),

    #  定义处理添加点赞的url地址响应方法，跳转到 likedView的addlikedact方法
    url(r'^addlikedact/$', likedViews.addlikedact, name='addlikedact'),

    #  定义跳转修改点赞的url地址响应方法，跳转到 likedView的updateliked方法
    url(r'^updateliked/(?P<id>[0-9]+)$', likedViews.updateliked, name='updateliked'),

    #  定义处理修改点赞的url地址响应方法，跳转到 likedView的updatelikedat方法
    url(r'^updatelikedact/$', likedViews.updatelikedact, name='updatelikedact'),

    #  定义跳转管理点赞的url地址响应方法，跳转到 likedView的likedmanage方法
    url(r'^likedmanage/$', likedViews.likedmanage, name='likedmanage'),

    #  定义跳转查看点赞的url地址响应方法，跳转到 likedView的likedview方法
    url(r'^likedview/$', likedViews.likedview, name='likedview'),

    #  定义处理删除点赞的url地址响应方法，跳转到 likedView的deleteliked方法
    url(r'^deletelikedact/(?P<id>[0-9]+)$', likedViews.deletelikedact, name='deletelikedact'),

    #  定义跳转搜索点赞的url地址响应方法，跳转到 likedView的searchliked方法
    url(r'^searchliked/$', likedViews.searchliked, name='searchliked'),

    #  定义点赞详情的url地址响应方法，跳转到 likedView的likeddetails方法
    url(r'^likeddetails/(?P<id>[0-9]+)$', likedViews.likeddetails, name='likeddetails'),

    #  定义添加点赞方法，响应页面请求，跳转到likedViews的useraddliked方法
    url(r'^useraddliked/$', likedViews.useraddliked, name='useraddliked'),

    #  定义处理添加点赞方法，响应页面请求，跳转到likedViews的useraddlikedact方法
    url(r'^useraddlikedact/$', likedViews.useraddlikedact, name='useraddlikedact'),

    #  定义跳转修改点赞方法，响应页面请求，跳转到likedViews的userupdateliked方法
    url(r'^userupdateliked/(?P<id>[0-9]+)$', likedViews.userupdateliked, name='userupdateliked'),

    #  定义处理修改点赞方法，响应页面请求，跳转到likedViews的userupdatelikedact方法
    url(r'^userupdatelikedact/$', likedViews.userupdatelikedact, name='userupdatelikedact'),

    #  定义跳转点赞管理方法，响应页面请求，跳转到likedViews的userlikedmanage方法
    url(r'^userlikedmanage/$', likedViews.userlikedmanage, name='userlikedmanage'),

    #  定义处理删除点赞方法，响应页面请求，跳转到likedViews的userdeleteliked方法
    url(r'^userdeletelikedact/(?P<id>[0-9]+)$', likedViews.userdeletelikedact, name='userdeletelikedact'),
]
