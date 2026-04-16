# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import articlecommentViews

urlpatterns = [

    #  定义添加文章评论的url地址响应方法，跳转到 articlecommentView的addarticlecomment方法
    url(r'^addarticlecomment/$', articlecommentViews.addarticlecomment, name='addarticlecomment'),

    url(r'^markCommentAsReadjson/$', articlecommentViews.markCommentAsReadjson, name='markCommentAsReadjson'),
    url(r'^getCommentNotificationsjson/$', articlecommentViews.getCommentNotificationsjson, name='getCommentNotificationsjson'),

    url(r'^addarticlecommentactjson/$', articlecommentViews.addarticlecommentactjson, name='addarticlecommentactjson'),

    #  定义处理添加文章评论的url地址响应方法，跳转到 articlecommentView的addarticlecommentact方法
    url(r'^addarticlecommentact/$', articlecommentViews.addarticlecommentact, name='addarticlecommentact'),

    #  定义跳转修改文章评论的url地址响应方法，跳转到 articlecommentView的updatearticlecomment方法
    url(r'^updatearticlecomment/(?P<id>[0-9]+)$', articlecommentViews.updatearticlecomment,
        name='updatearticlecomment'),

    #  定义处理修改文章评论的url地址响应方法，跳转到 articlecommentView的updatearticlecommentat方法
    url(r'^updatearticlecommentact/$', articlecommentViews.updatearticlecommentact, name='updatearticlecommentact'),

    #  定义跳转管理文章评论的url地址响应方法，跳转到 articlecommentView的articlecommentmanage方法
    url(r'^articlecommentmanage/$', articlecommentViews.articlecommentmanage, name='articlecommentmanage'),

    #  定义跳转查看文章评论的url地址响应方法，跳转到 articlecommentView的articlecommentview方法
    url(r'^articlecommentview/$', articlecommentViews.articlecommentview, name='articlecommentview'),

    #  定义处理删除文章评论的url地址响应方法，跳转到 articlecommentView的deletearticlecomment方法
    url(r'^deletearticlecommentact/(?P<id>[0-9]+)$', articlecommentViews.deletearticlecommentact,
        name='deletearticlecommentact'),

    #  定义跳转搜索文章评论的url地址响应方法，跳转到 articlecommentView的searcharticlecomment方法
    url(r'^searcharticlecomment/$', articlecommentViews.searcharticlecomment, name='searcharticlecomment'),

    #  定义文章评论详情的url地址响应方法，跳转到 articlecommentView的articlecommentdetails方法
    url(r'^articlecommentdetails/(?P<id>[0-9]+)$', articlecommentViews.articlecommentdetails,
        name='articlecommentdetails'),

    #  定义添加文章评论方法，响应页面请求，跳转到articlecommentViews的useraddarticlecomment方法
    url(r'^useraddarticlecomment/$', articlecommentViews.useraddarticlecomment, name='useraddarticlecomment'),

    #  定义处理添加文章评论方法，响应页面请求，跳转到articlecommentViews的useraddarticlecommentact方法
    url(r'^useraddarticlecommentact/$', articlecommentViews.useraddarticlecommentact, name='useraddarticlecommentact'),

    #  定义跳转修改文章评论方法，响应页面请求，跳转到articlecommentViews的userupdatearticlecomment方法
    url(r'^userupdatearticlecomment/(?P<id>[0-9]+)$', articlecommentViews.userupdatearticlecomment,
        name='userupdatearticlecomment'),

    #  定义处理修改文章评论方法，响应页面请求，跳转到articlecommentViews的userupdatearticlecommentact方法
    url(r'^userupdatearticlecommentact/$', articlecommentViews.userupdatearticlecommentact,
        name='userupdatearticlecommentact'),

    #  定义跳转文章评论管理方法，响应页面请求，跳转到articlecommentViews的userarticlecommentmanage方法
    url(r'^userarticlecommentmanage/$', articlecommentViews.userarticlecommentmanage, name='userarticlecommentmanage'),

    #  定义处理删除文章评论方法，响应页面请求，跳转到articlecommentViews的userdeletearticlecomment方法
    url(r'^userdeletearticlecommentact/(?P<id>[0-9]+)$', articlecommentViews.userdeletearticlecommentact,
        name='userdeletearticlecommentact'),

    url(r'^searcharticlecommentjson/$', articlecommentViews.searcharticlecommentjson, name='searcharticlecommentjson'),
    # url('searcharticlecommentjson/', articlecommentViews.searcharticlecommentjson, name='searcharticlecommentjson'),
]
