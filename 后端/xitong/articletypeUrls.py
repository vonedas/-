# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import articletypeViews

urlpatterns = [

    #  定义添加文章分类的url地址响应方法，跳转到 articletypeView的addarticletype方法
    url(r'^addarticletype/$', articletypeViews.addarticletype, name='addarticletype'),

    #  定义处理添加文章分类的url地址响应方法，跳转到 articletypeView的addarticletypeact方法
    url(r'^addarticletypeact/$', articletypeViews.addarticletypeact, name='addarticletypeact'),

    url(r'^searcharticletypejson/$', articletypeViews.searcharticletypejson, name='searcharticletypejson'),

    #  定义跳转修改文章分类的url地址响应方法，跳转到 articletypeView的updatearticletype方法
    url(r'^updatearticletype/(?P<id>[0-9]+)$', articletypeViews.updatearticletype, name='updatearticletype'),

    #  定义处理修改文章分类的url地址响应方法，跳转到 articletypeView的updatearticletypeat方法
    url(r'^updatearticletypeact/$', articletypeViews.updatearticletypeact, name='updatearticletypeact'),

    #  定义跳转管理文章分类的url地址响应方法，跳转到 articletypeView的articletypemanage方法
    url(r'^articletypemanage/$', articletypeViews.articletypemanage, name='articletypemanage'),

    #  定义跳转查看文章分类的url地址响应方法，跳转到 articletypeView的articletypeview方法
    url(r'^articletypeview/$', articletypeViews.articletypeview, name='articletypeview'),

    #  定义处理删除文章分类的url地址响应方法，跳转到 articletypeView的deletearticletype方法
    url(r'^deletearticletypeact/(?P<id>[0-9]+)$', articletypeViews.deletearticletypeact, name='deletearticletypeact'),

    #  定义跳转搜索文章分类的url地址响应方法，跳转到 articletypeView的searcharticletype方法
    url(r'^searcharticletype/$', articletypeViews.searcharticletype, name='searcharticletype'),

    #  定义文章分类详情的url地址响应方法，跳转到 articletypeView的articletypedetails方法
    url(r'^articletypedetails/(?P<id>[0-9]+)$', articletypeViews.articletypedetails, name='articletypedetails'),
]
