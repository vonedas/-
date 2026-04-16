# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import zinvViews

urlpatterns = [

    #  定义添加子女的url地址响应方法，跳转到 zinvView的addzinv方法
    url(r'^addzinv/$', zinvViews.addzinv, name='addzinv'),

    #  定义处理添加子女的url地址响应方法，跳转到 zinvView的addzinvact方法
    url(r'^addzinvact/$', zinvViews.addzinvact, name='addzinvact'),

    #  定义跳转修改子女的url地址响应方法，跳转到 zinvView的updatezinv方法
    url(r'^updatezinv/(?P<id>[0-9]+)$', zinvViews.updatezinv, name='updatezinv'),

    #  定义处理修改子女的url地址响应方法，跳转到 zinvView的updatezinvat方法
    url(r'^updatezinvact/$', zinvViews.updatezinvact, name='updatezinvact'),

    #  定义跳转管理子女的url地址响应方法，跳转到 zinvView的zinvmanage方法
    url(r'^zinvmanage/$', zinvViews.zinvmanage, name='zinvmanage'),

    #  定义跳转查看子女的url地址响应方法，跳转到 zinvView的zinvview方法
    url(r'^zinvview/$', zinvViews.zinvview, name='zinvview'),

    #  定义处理删除子女的url地址响应方法，跳转到 zinvView的deletezinv方法
    url(r'^deletezinvact/(?P<id>[0-9]+)$', zinvViews.deletezinvact, name='deletezinvact'),

    #  定义跳转搜索子女的url地址响应方法，跳转到 zinvView的searchzinv方法
    url(r'^searchzinv/$', zinvViews.searchzinv, name='searchzinv'),

    #  定义子女详情的url地址响应方法，跳转到 zinvView的zinvdetails方法
    url(r'^zinvdetails/(?P<id>[0-9]+)$', zinvViews.zinvdetails, name='zinvdetails'),
]
