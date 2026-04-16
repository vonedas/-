# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import collectedViews

urlpatterns = [

    #  定义添加收藏的url地址响应方法，跳转到 collectedView的addcollected方法
    url(r'^addcollected/$', collectedViews.addcollected, name='addcollected'),

    #  定义处理添加收藏的url地址响应方法，跳转到 collectedView的addcollectedact方法
    url(r'^addcollectedact/$', collectedViews.addcollectedact, name='addcollectedact'),

    #  定义跳转修改收藏的url地址响应方法，跳转到 collectedView的updatecollected方法
    url(r'^updatecollected/(?P<id>[0-9]+)$', collectedViews.updatecollected, name='updatecollected'),

    #  定义处理修改收藏的url地址响应方法，跳转到 collectedView的updatecollectedat方法
    url(r'^updatecollectedact/$', collectedViews.updatecollectedact, name='updatecollectedact'),

    #  定义跳转管理收藏的url地址响应方法，跳转到 collectedView的collectedmanage方法
    url(r'^collectedmanage/$', collectedViews.collectedmanage, name='collectedmanage'),

    #  定义跳转查看收藏的url地址响应方法，跳转到 collectedView的collectedview方法
    url(r'^collectedview/$', collectedViews.collectedview, name='collectedview'),

    #  定义处理删除收藏的url地址响应方法，跳转到 collectedView的deletecollected方法
    url(r'^deletecollectedact/(?P<id>[0-9]+)$', collectedViews.deletecollectedact, name='deletecollectedact'),

    #  定义跳转搜索收藏的url地址响应方法，跳转到 collectedView的searchcollected方法
    url(r'^searchcollected/$', collectedViews.searchcollected, name='searchcollected'),

    #  定义收藏详情的url地址响应方法，跳转到 collectedView的collecteddetails方法
    url(r'^collecteddetails/(?P<id>[0-9]+)$', collectedViews.collecteddetails, name='collecteddetails'),

    #  定义添加收藏方法，响应页面请求，跳转到collectedViews的useraddcollected方法
    url(r'^useraddcollected/$', collectedViews.useraddcollected, name='useraddcollected'),

    #  定义处理添加收藏方法，响应页面请求，跳转到collectedViews的useraddcollectedact方法
    url(r'^useraddcollectedact/$', collectedViews.useraddcollectedact, name='useraddcollectedact'),

    #  定义跳转修改收藏方法，响应页面请求，跳转到collectedViews的userupdatecollected方法
    url(r'^userupdatecollected/(?P<id>[0-9]+)$', collectedViews.userupdatecollected, name='userupdatecollected'),

    #  定义处理修改收藏方法，响应页面请求，跳转到collectedViews的userupdatecollectedact方法
    url(r'^userupdatecollectedact/$', collectedViews.userupdatecollectedact, name='userupdatecollectedact'),

    #  定义跳转收藏管理方法，响应页面请求，跳转到collectedViews的usercollectedmanage方法
    url(r'^usercollectedmanage/$', collectedViews.usercollectedmanage, name='usercollectedmanage'),

    #  定义处理删除收藏方法，响应页面请求，跳转到collectedViews的userdeletecollected方法
    url(r'^userdeletecollectedact/(?P<id>[0-9]+)$', collectedViews.userdeletecollectedact,
        name='userdeletecollectedact'),
]
