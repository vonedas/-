# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import bangdingViews

urlpatterns = [

    #  定义添加绑定的url地址响应方法，跳转到 bangdingView的addbangding方法
    url(r'^addbangding/$', bangdingViews.addbangding, name='addbangding'),

    #  定义处理添加绑定的url地址响应方法，跳转到 bangdingView的addbangdingact方法
    url(r'^addbangdingact/$', bangdingViews.addbangdingact, name='addbangdingact'),

    #  定义跳转修改绑定的url地址响应方法，跳转到 bangdingView的updatebangding方法
    url(r'^updatebangding/(?P<id>[0-9]+)$', bangdingViews.updatebangding, name='updatebangding'),

    #  定义处理修改绑定的url地址响应方法，跳转到 bangdingView的updatebangdingat方法
    url(r'^updatebangdingact/$', bangdingViews.updatebangdingact, name='updatebangdingact'),

    #  定义跳转管理绑定的url地址响应方法，跳转到 bangdingView的bangdingmanage方法
    url(r'^bangdingmanage/$', bangdingViews.bangdingmanage, name='bangdingmanage'),

    #  定义跳转查看绑定的url地址响应方法，跳转到 bangdingView的bangdingview方法
    url(r'^bangdingview/$', bangdingViews.bangdingview, name='bangdingview'),

    #  定义处理删除绑定的url地址响应方法，跳转到 bangdingView的deletebangding方法
    url(r'^deletebangdingact/(?P<id>[0-9]+)$', bangdingViews.deletebangdingact, name='deletebangdingact'),

    #  定义跳转搜索绑定的url地址响应方法，跳转到 bangdingView的searchbangding方法
    url(r'^searchbangding/$', bangdingViews.searchbangding, name='searchbangding'),

    #  定义绑定详情的url地址响应方法，跳转到 bangdingView的bangdingdetails方法
    url(r'^bangdingdetails/(?P<id>[0-9]+)$', bangdingViews.bangdingdetails, name='bangdingdetails'),

    #  定义添加绑定方法，响应页面请求，跳转到bangdingViews的zinvaddbangding方法
    url(r'^zinvaddbangding/$', bangdingViews.zinvaddbangding, name='zinvaddbangding'),

    #  定义处理添加绑定方法，响应页面请求，跳转到bangdingViews的zinvaddbangdingact方法
    url(r'^zinvaddbangdingact/$', bangdingViews.zinvaddbangdingact, name='zinvaddbangdingact'),

    #  定义跳转修改绑定方法，响应页面请求，跳转到bangdingViews的zinvupdatebangding方法
    url(r'^zinvupdatebangding/(?P<id>[0-9]+)$', bangdingViews.zinvupdatebangding, name='zinvupdatebangding'),

    #  定义处理修改绑定方法，响应页面请求，跳转到bangdingViews的zinvupdatebangdingact方法
    url(r'^zinvupdatebangdingact/$', bangdingViews.zinvupdatebangdingact, name='zinvupdatebangdingact'),

    #  定义跳转绑定管理方法，响应页面请求，跳转到bangdingViews的zinvbangdingmanage方法
    url(r'^zinvbangdingmanage/$', bangdingViews.zinvbangdingmanage, name='zinvbangdingmanage'),

    #  定义处理删除绑定方法，响应页面请求，跳转到bangdingViews的zinvdeletebangding方法
    url(r'^zinvdeletebangdingact/(?P<id>[0-9]+)$', bangdingViews.zinvdeletebangdingact, name='zinvdeletebangdingact'),
]
