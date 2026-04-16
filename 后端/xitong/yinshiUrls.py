# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import yinshiViews

urlpatterns = [

    #  定义添加饮食剩余的url地址响应方法，跳转到 yinshiView的addyinshi方法
    url(r'^addyinshi/$', yinshiViews.addyinshi, name='addyinshi'),

    #  定义处理添加饮食剩余的url地址响应方法，跳转到 yinshiView的addyinshiact方法
    url(r'^addyinshiact/$', yinshiViews.addyinshiact, name='addyinshiact'),

    #  定义跳转修改饮食剩余的url地址响应方法，跳转到 yinshiView的updateyinshi方法
    url(r'^updateyinshi/(?P<id>[0-9]+)$', yinshiViews.updateyinshi, name='updateyinshi'),

    #  定义处理修改饮食剩余的url地址响应方法，跳转到 yinshiView的updateyinshiat方法
    url(r'^updateyinshiact/$', yinshiViews.updateyinshiact, name='updateyinshiact'),

    #  定义跳转管理饮食剩余的url地址响应方法，跳转到 yinshiView的yinshimanage方法
    url(r'^yinshimanage/$', yinshiViews.yinshimanage, name='yinshimanage'),

    #  定义跳转查看饮食剩余的url地址响应方法，跳转到 yinshiView的yinshiview方法
    url(r'^yinshiview/$', yinshiViews.yinshiview, name='yinshiview'),

    #  定义处理删除饮食剩余的url地址响应方法，跳转到 yinshiView的deleteyinshi方法
    url(r'^deleteyinshiact/(?P<id>[0-9]+)$', yinshiViews.deleteyinshiact, name='deleteyinshiact'),

    #  定义跳转搜索饮食剩余的url地址响应方法，跳转到 yinshiView的searchyinshi方法
    url(r'^searchyinshi/$', yinshiViews.searchyinshi, name='searchyinshi'),

    #  定义饮食剩余详情的url地址响应方法，跳转到 yinshiView的yinshidetails方法
    url(r'^yinshidetails/(?P<id>[0-9]+)$', yinshiViews.yinshidetails, name='yinshidetails'),

    #  定义添加饮食剩余方法，响应页面请求，跳转到yinshiViews的useraddyinshi方法
    url(r'^useraddyinshi/$', yinshiViews.useraddyinshi, name='useraddyinshi'),

    #  定义处理添加饮食剩余方法，响应页面请求，跳转到yinshiViews的useraddyinshiact方法
    url(r'^useraddyinshiact/$', yinshiViews.useraddyinshiact, name='useraddyinshiact'),

    #  定义跳转修改饮食剩余方法，响应页面请求，跳转到yinshiViews的userupdateyinshi方法
    url(r'^userupdateyinshi/(?P<id>[0-9]+)$', yinshiViews.userupdateyinshi, name='userupdateyinshi'),

    #  定义处理修改饮食剩余方法，响应页面请求，跳转到yinshiViews的userupdateyinshiact方法
    url(r'^userupdateyinshiact/$', yinshiViews.userupdateyinshiact, name='userupdateyinshiact'),

    #  定义跳转饮食剩余管理方法，响应页面请求，跳转到yinshiViews的useryinshimanage方法
    url(r'^useryinshimanage/$', yinshiViews.useryinshimanage, name='useryinshimanage'),

    #  定义处理删除饮食剩余方法，响应页面请求，跳转到yinshiViews的userdeleteyinshi方法
    url(r'^userdeleteyinshiact/(?P<id>[0-9]+)$', yinshiViews.userdeleteyinshiact, name='userdeleteyinshiact'),
]
