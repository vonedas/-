# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import duanlianlogViews

urlpatterns = [

    #  定义添加锻炼记录的url地址响应方法，跳转到 duanlianlogView的addduanlianlog方法
    url(r'^addduanlianlog/$', duanlianlogViews.addduanlianlog, name='addduanlianlog'),

    #  定义处理添加锻炼记录的url地址响应方法，跳转到 duanlianlogView的addduanlianlogact方法
    url(r'^addduanlianlogact/$', duanlianlogViews.addduanlianlogact, name='addduanlianlogact'),

    #  定义跳转修改锻炼记录的url地址响应方法，跳转到 duanlianlogView的updateduanlianlog方法
    url(r'^updateduanlianlog/(?P<id>[0-9]+)$', duanlianlogViews.updateduanlianlog, name='updateduanlianlog'),

    #  定义处理修改锻炼记录的url地址响应方法，跳转到 duanlianlogView的updateduanlianlogat方法
    url(r'^updateduanlianlogact/$', duanlianlogViews.updateduanlianlogact, name='updateduanlianlogact'),

    #  定义跳转管理锻炼记录的url地址响应方法，跳转到 duanlianlogView的duanlianlogmanage方法
    url(r'^duanlianlogmanage/$', duanlianlogViews.duanlianlogmanage, name='duanlianlogmanage'),

    #  定义跳转查看锻炼记录的url地址响应方法，跳转到 duanlianlogView的duanlianlogview方法
    url(r'^duanlianlogview/$', duanlianlogViews.duanlianlogview, name='duanlianlogview'),

    #  定义处理删除锻炼记录的url地址响应方法，跳转到 duanlianlogView的deleteduanlianlog方法
    url(r'^deleteduanlianlogact/(?P<id>[0-9]+)$', duanlianlogViews.deleteduanlianlogact, name='deleteduanlianlogact'),

    #  定义跳转搜索锻炼记录的url地址响应方法，跳转到 duanlianlogView的searchduanlianlog方法
    url(r'^searchduanlianlog/$', duanlianlogViews.searchduanlianlog, name='searchduanlianlog'),

    #  定义锻炼记录详情的url地址响应方法，跳转到 duanlianlogView的duanlianlogdetails方法
    url(r'^duanlianlogdetails/(?P<id>[0-9]+)$', duanlianlogViews.duanlianlogdetails, name='duanlianlogdetails'),

    #  定义添加锻炼记录方法，响应页面请求，跳转到duanlianlogViews的useraddduanlianlog方法
    url(r'^useraddduanlianlog/$', duanlianlogViews.useraddduanlianlog, name='useraddduanlianlog'),

    #  定义处理添加锻炼记录方法，响应页面请求，跳转到duanlianlogViews的useraddduanlianlogact方法
    url(r'^useraddduanlianlogact/$', duanlianlogViews.useraddduanlianlogact, name='useraddduanlianlogact'),

    #  定义跳转修改锻炼记录方法，响应页面请求，跳转到duanlianlogViews的userupdateduanlianlog方法
    url(r'^userupdateduanlianlog/(?P<id>[0-9]+)$', duanlianlogViews.userupdateduanlianlog,
        name='userupdateduanlianlog'),

    #  定义处理修改锻炼记录方法，响应页面请求，跳转到duanlianlogViews的userupdateduanlianlogact方法
    url(r'^userupdateduanlianlogact/$', duanlianlogViews.userupdateduanlianlogact, name='userupdateduanlianlogact'),

    #  定义跳转锻炼记录管理方法，响应页面请求，跳转到duanlianlogViews的userduanlianlogmanage方法
    url(r'^userduanlianlogmanage/$', duanlianlogViews.userduanlianlogmanage, name='userduanlianlogmanage'),

    #  定义处理删除锻炼记录方法，响应页面请求，跳转到duanlianlogViews的userdeleteduanlianlog方法
    url(r'^userdeleteduanlianlogact/(?P<id>[0-9]+)$', duanlianlogViews.userdeleteduanlianlogact,
        name='userdeleteduanlianlogact'),

    # 获取运动类型列表
    url(r'^getMotionTypes/$', duanlianlogViews.getMotionTypes, name='getMotionTypes'),

    # 计算卡路里
    url(r'^calculateCalories/$', duanlianlogViews.calculateCalories, name='calculateCalories'),
]
