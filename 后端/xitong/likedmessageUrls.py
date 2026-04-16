# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from  . import likedmessageViews
urlpatterns = [

#  定义添加点赞通知的url地址响应方法，跳转到 likedmessageView的addlikedmessage方法     
    url(r'^addlikedmessage/$', likedmessageViews.addlikedmessage, name='addlikedmessage'),

    url(r'^getLikeNotificationsjson/$', likedmessageViews.getLikeNotificationsjson, name='getLikeNotificationsjson'),


    url(r'^markLikeAsReadjson/$', likedmessageViews.markLikeAsReadjson, name='markLikeAsReadjson'),
#  定义处理添加点赞通知的url地址响应方法，跳转到 likedmessageView的addlikedmessageact方法     
    url(r'^addlikedmessageact/$', likedmessageViews.addlikedmessageact, name='addlikedmessageact'),

    url(r'^addlikedmessageactjson/$', likedmessageViews.addlikedmessageactjson, name='addlikedmessageactjson'),

    url(r'^deletelikedmessagejson/$', likedmessageViews.deletelikedmessagejson, name='deletelikedmessagejson'),

    url(r'^searchlikedmessagejson/$', likedmessageViews.searchlikedmessagejson, name='searchlikedmessagejson'),

#  定义跳转修改点赞通知的url地址响应方法，跳转到 likedmessageView的updatelikedmessage方法     
    url(r'^updatelikedmessage/(?P<id>[0-9]+)$', likedmessageViews.updatelikedmessage, name='updatelikedmessage'),

#  定义处理修改点赞通知的url地址响应方法，跳转到 likedmessageView的updatelikedmessageat方法     
    url(r'^updatelikedmessageact/$', likedmessageViews.updatelikedmessageact, name='updatelikedmessageact'),

#  定义跳转管理点赞通知的url地址响应方法，跳转到 likedmessageView的likedmessagemanage方法     
    url(r'^likedmessagemanage/$', likedmessageViews.likedmessagemanage, name='likedmessagemanage'),

#  定义跳转查看点赞通知的url地址响应方法，跳转到 likedmessageView的likedmessageview方法     
    url(r'^likedmessageview/$', likedmessageViews.likedmessageview, name='likedmessageview'),

#  定义处理删除点赞通知的url地址响应方法，跳转到 likedmessageView的deletelikedmessage方法     
    url(r'^deletelikedmessageact/(?P<id>[0-9]+)$', likedmessageViews.deletelikedmessageact, name='deletelikedmessageact'),

#  定义跳转搜索点赞通知的url地址响应方法，跳转到 likedmessageView的searchlikedmessage方法     
    url(r'^searchlikedmessage/$', likedmessageViews.searchlikedmessage, name='searchlikedmessage'),

#  定义点赞通知详情的url地址响应方法，跳转到 likedmessageView的likedmessagedetails方法     
    url(r'^likedmessagedetails/(?P<id>[0-9]+)$', likedmessageViews.likedmessagedetails, name='likedmessagedetails'),
]

