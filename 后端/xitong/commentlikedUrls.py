# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import commentlikedViews

urlpatterns = [

    #  定义添加评论点赞的url地址响应方法，跳转到 commentlikedView的addcommentliked方法
    url(r'^addcommentliked/$', commentlikedViews.addcommentliked, name='addcommentliked'),

    #  定义处理添加评论点赞的url地址响应方法，跳转到 commentlikedView的addcommentlikedact方法
    url(r'^addcommentlikedact/$', commentlikedViews.addcommentlikedact, name='addcommentlikedact'),

    #  定义跳转修改评论点赞的url地址响应方法，跳转到 commentlikedView的updatecommentliked方法
    url(r'^updatecommentliked/(?P<id>[0-9]+)$', commentlikedViews.updatecommentliked, name='updatecommentliked'),

    #  定义处理修改评论点赞的url地址响应方法，跳转到 commentlikedView的updatecommentlikedat方法
    url(r'^updatecommentlikedact/$', commentlikedViews.updatecommentlikedact, name='updatecommentlikedact'),

    #  定义跳转管理评论点赞的url地址响应方法，跳转到 commentlikedView的commentlikedmanage方法
    url(r'^commentlikedmanage/$', commentlikedViews.commentlikedmanage, name='commentlikedmanage'),

    #  定义跳转查看评论点赞的url地址响应方法，跳转到 commentlikedView的commentlikedview方法
    url(r'^commentlikedview/$', commentlikedViews.commentlikedview, name='commentlikedview'),

    #  定义处理删除评论点赞的url地址响应方法，跳转到 commentlikedView的deletecommentliked方法
    url(r'^deletecommentlikedact/(?P<id>[0-9]+)$', commentlikedViews.deletecommentlikedact,
        name='deletecommentlikedact'),

    #  定义跳转搜索评论点赞的url地址响应方法，跳转到 commentlikedView的searchcommentliked方法
    url(r'^searchcommentliked/$', commentlikedViews.searchcommentliked, name='searchcommentliked'),

    #  定义评论点赞详情的url地址响应方法，跳转到 commentlikedView的commentlikeddetails方法
    url(r'^commentlikeddetails/(?P<id>[0-9]+)$', commentlikedViews.commentlikeddetails, name='commentlikeddetails'),

    #  定义添加评论点赞方法，响应页面请求，跳转到commentlikedViews的useraddcommentliked方法
    url(r'^useraddcommentliked/$', commentlikedViews.useraddcommentliked, name='useraddcommentliked'),

    #  定义处理添加评论点赞方法，响应页面请求，跳转到commentlikedViews的useraddcommentlikedact方法
    url(r'^useraddcommentlikedact/$', commentlikedViews.useraddcommentlikedact, name='useraddcommentlikedact'),

    #  定义跳转修改评论点赞方法，响应页面请求，跳转到commentlikedViews的userupdatecommentliked方法
    url(r'^userupdatecommentliked/(?P<id>[0-9]+)$', commentlikedViews.userupdatecommentliked,
        name='userupdatecommentliked'),

    #  定义处理修改评论点赞方法，响应页面请求，跳转到commentlikedViews的userupdatecommentlikedact方法
    url(r'^userupdatecommentlikedact/$', commentlikedViews.userupdatecommentlikedact, name='userupdatecommentlikedact'),

    #  定义跳转评论点赞管理方法，响应页面请求，跳转到commentlikedViews的usercommentlikedmanage方法
    url(r'^usercommentlikedmanage/$', commentlikedViews.usercommentlikedmanage, name='usercommentlikedmanage'),

    #  定义处理删除评论点赞方法，响应页面请求，跳转到commentlikedViews的userdeletecommentliked方法
    url(r'^userdeletecommentlikedact/(?P<id>[0-9]+)$', commentlikedViews.userdeletecommentlikedact,
        name='userdeletecommentlikedact'),

    url(r'^commentlikedjson/$', commentlikedViews.commentlikedjson, name='commentlikedjson'),
    url(r'^addcommentlikedjson/$', commentlikedViews.addcommentlikedjson, name='addcommentlikedjson'),
    url(r'^cancelcommentlikedjson/$', commentlikedViews.cancelcommentlikedjson, name='cancelcommentlikedjson'),
]
