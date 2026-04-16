# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import userViews

urlpatterns = [

    #  定义添加用户的url地址响应方法，跳转到 userView的adduser方法
    url(r'^adduser/$', userViews.adduser, name='adduser'),

    #  定义处理添加用户的url地址响应方法，跳转到 userView的adduseract方法
    url(r'^adduseract/$', userViews.adduseract, name='adduseract'),

    url(r'^searchuserjson2/$', userViews.searchuserjson2, name='searchuserjson2'),


    url(r'^updateuseractjson/$', userViews.updateuseractjson, name='updateuseractjson'),

    #  定义跳转修改用户的url地址响应方法，跳转到 userView的updateuser方法
    url(r'^updateuser/(?P<id>[0-9]+)$', userViews.updateuser, name='updateuser'),

    #  定义处理修改用户的url地址响应方法，跳转到 userView的updateuserat方法
    url(r'^updateuseract/$', userViews.updateuseract, name='updateuseract'),

    #  定义跳转管理用户的url地址响应方法，跳转到 userView的usermanage方法
    url(r'^usermanage/$', userViews.usermanage, name='usermanage'),

    #  定义跳转查看用户的url地址响应方法，跳转到 userView的userview方法
    url(r'^userview/$', userViews.userview, name='userview'),

    #  定义处理删除用户的url地址响应方法，跳转到 userView的deleteuser方法
    url(r'^deleteuseract/(?P<id>[0-9]+)$', userViews.deleteuseract, name='deleteuseract'),

    #  定义跳转搜索用户的url地址响应方法，跳转到 userView的searchuser方法
    url(r'^searchuser/$', userViews.searchuser, name='searchuser'),

    #  定义用户详情的url地址响应方法，跳转到 userView的userdetails方法
    url(r'^userdetails/(?P<id>[0-9]+)$', userViews.userdetails, name='userdetails'),

    url(r'^getmessage/$', userViews.getmessage, name='getmessage'),
    url(r'^attention/$', userViews.attention, name='attention'),
    url(r'^yao/$', userViews.yao, name='yao'),
    url(r'^getauth/$', userViews.getauth, name='getauth'),
    url(r'^saveauth/$', userViews.saveauth, name='saveauth'),
]
