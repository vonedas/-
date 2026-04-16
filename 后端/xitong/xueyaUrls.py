# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import xueyaViews

urlpatterns = [

    #  定义添加血压的url地址响应方法，跳转到 xueyaView的addxueya方法
    url(r'^addxueya/$', xueyaViews.addxueya, name='addxueya'),

    #  定义处理添加血压的url地址响应方法，跳转到 xueyaView的addxueyaact方法
    url(r'^addxueyaact/$', xueyaViews.addxueyaact, name='addxueyaact'),

    #  定义跳转修改血压的url地址响应方法，跳转到 xueyaView的updatexueya方法
    url(r'^updatexueya/(?P<id>[0-9]+)$', xueyaViews.updatexueya, name='updatexueya'),

    #  定义处理修改血压的url地址响应方法，跳转到 xueyaView的updatexueyaat方法
    url(r'^updatexueyaact/$', xueyaViews.updatexueyaact, name='updatexueyaact'),

    #  定义跳转管理血压的url地址响应方法，跳转到 xueyaView的xueyamanage方法
    url(r'^xueyamanage/$', xueyaViews.xueyamanage, name='xueyamanage'),

    #  定义跳转查看血压的url地址响应方法，跳转到 xueyaView的xueyaview方法
    url(r'^xueyaview/$', xueyaViews.xueyaview, name='xueyaview'),

    #  定义处理删除血压的url地址响应方法，跳转到 xueyaView的deletexueya方法
    url(r'^deletexueyaact/(?P<id>[0-9]+)$', xueyaViews.deletexueyaact, name='deletexueyaact'),

    #  定义跳转搜索血压的url地址响应方法，跳转到 xueyaView的searchxueya方法
    url(r'^searchxueya/$', xueyaViews.searchxueya, name='searchxueya'),

    #  定义血压详情的url地址响应方法，跳转到 xueyaView的xueyadetails方法
    url(r'^xueyadetails/(?P<id>[0-9]+)$', xueyaViews.xueyadetails, name='xueyadetails'),

    #  定义添加血压方法，响应页面请求，跳转到xueyaViews的useraddxueya方法
    url(r'^useraddxueya/$', xueyaViews.useraddxueya, name='useraddxueya'),

    #  定义处理添加血压方法，响应页面请求，跳转到xueyaViews的useraddxueyaact方法
    url(r'^useraddxueyaact/$', xueyaViews.useraddxueyaact, name='useraddxueyaact'),

    #  定义跳转修改血压方法，响应页面请求，跳转到xueyaViews的userupdatexueya方法
    url(r'^userupdatexueya/(?P<id>[0-9]+)$', xueyaViews.userupdatexueya, name='userupdatexueya'),

    #  定义处理修改血压方法，响应页面请求，跳转到xueyaViews的userupdatexueyaact方法
    url(r'^userupdatexueyaact/$', xueyaViews.userupdatexueyaact, name='userupdatexueyaact'),

    #  定义跳转血压管理方法，响应页面请求，跳转到xueyaViews的userxueyamanage方法
    url(r'^userxueyamanage/$', xueyaViews.userxueyamanage, name='userxueyamanage'),

    #  定义处理删除血压方法，响应页面请求，跳转到xueyaViews的userdeletexueya方法
    url(r'^userdeletexueyaact/(?P<id>[0-9]+)$', xueyaViews.userdeletexueyaact, name='userdeletexueyaact'),
]
