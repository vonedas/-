# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import yinshilogViews

urlpatterns = [

    #  定义添加饮食记录的url地址响应方法，跳转到 yinshilogView的addyinshilog方法
    url(r'^addyinshilog/$', yinshilogViews.addyinshilog, name='addyinshilog'),

    #  定义处理添加饮食记录的url地址响应方法，跳转到 yinshilogView的addyinshilogact方法
    url(r'^addyinshilogact/$', yinshilogViews.addyinshilogact, name='addyinshilogact'),

    #  定义跳转修改饮食记录的url地址响应方法，跳转到 yinshilogView的updateyinshilog方法
    url(r'^updateyinshilog/(?P<id>[0-9]+)$', yinshilogViews.updateyinshilog, name='updateyinshilog'),

    #  定义处理修改饮食记录的url地址响应方法，跳转到 yinshilogView的updateyinshilogat方法
    url(r'^updateyinshilogact/$', yinshilogViews.updateyinshilogact, name='updateyinshilogact'),

    #  定义跳转管理饮食记录的url地址响应方法，跳转到 yinshilogView的yinshilogmanage方法
    url(r'^yinshilogmanage/$', yinshilogViews.yinshilogmanage, name='yinshilogmanage'),

    #  定义跳转查看饮食记录的url地址响应方法，跳转到 yinshilogView的yinshilogview方法
    url(r'^yinshilogview/$', yinshilogViews.yinshilogview, name='yinshilogview'),

    #  定义处理删除饮食记录的url地址响应方法，跳转到 yinshilogView的deleteyinshilog方法
    url(r'^deleteyinshilogact/(?P<id>[0-9]+)$', yinshilogViews.deleteyinshilogact, name='deleteyinshilogact'),

    #  定义跳转搜索饮食记录的url地址响应方法，跳转到 yinshilogView的searchyinshilog方法
    url(r'^searchyinshilog/$', yinshilogViews.searchyinshilog, name='searchyinshilog'),

    #  定义饮食记录详情的url地址响应方法，跳转到 yinshilogView的yinshilogdetails方法
    url(r'^yinshilogdetails/(?P<id>[0-9]+)$', yinshilogViews.yinshilogdetails, name='yinshilogdetails'),

    #  定义添加饮食记录方法，响应页面请求，跳转到yinshilogViews的useraddyinshilog方法
    url(r'^useraddyinshilog/$', yinshilogViews.useraddyinshilog, name='useraddyinshilog'),

    #  定义处理添加饮食记录方法，响应页面请求，跳转到yinshilogViews的useraddyinshilogact方法
    url(r'^useraddyinshilogact/$', yinshilogViews.useraddyinshilogact, name='useraddyinshilogact'),

    #  定义跳转修改饮食记录方法，响应页面请求，跳转到yinshilogViews的userupdateyinshilog方法
    url(r'^userupdateyinshilog/(?P<id>[0-9]+)$', yinshilogViews.userupdateyinshilog, name='userupdateyinshilog'),

    #  定义处理修改饮食记录方法，响应页面请求，跳转到yinshilogViews的userupdateyinshilogact方法
    url(r'^userupdateyinshilogact/$', yinshilogViews.userupdateyinshilogact, name='userupdateyinshilogact'),

    #  定义跳转饮食记录管理方法，响应页面请求，跳转到yinshilogViews的useryinshilogmanage方法
    url(r'^useryinshilogmanage/$', yinshilogViews.useryinshilogmanage, name='useryinshilogmanage'),

    #  定义处理删除饮食记录方法，响应页面请求，跳转到yinshilogViews的userdeleteyinshilog方法
    url(r'^userdeleteyinshilogact/(?P<id>[0-9]+)$', yinshilogViews.userdeleteyinshilogact,
        name='userdeleteyinshilogact'),
]
