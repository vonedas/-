# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import motiontypeViews

urlpatterns = [

    #  定义添加运动类型的url地址响应方法，跳转到 motiontypeView的addmotiontype方法
    url(r'^addmotiontype/$', motiontypeViews.addmotiontype, name='addmotiontype'),


    url(r'^deletemotiontypejson/$', motiontypeViews.deletemotiontypejson, name='deletemotiontypejson'),

    url(r'^searchmotiontypejson/$', motiontypeViews.searchmotiontypejson, name='searchmotiontypejson'),

    url(r'^usersearchmotiontypejson/$', motiontypeViews.usersearchmotiontypejson, name='usersearchmotiontypejson'),

    #  定义处理添加运动类型的url地址响应方法，跳转到 motiontypeView的addmotiontypeact方法
    url(r'^addmotiontypeact/$', motiontypeViews.addmotiontypeact, name='addmotiontypeact'),

    url(r'^addmotiontypeactjson/$', motiontypeViews.addmotiontypeactjson, name='addmotiontypeactjson'),

    #  定义跳转修改运动类型的url地址响应方法，跳转到 motiontypeView的updatemotiontype方法
    url(r'^updatemotiontype/(?P<id>[0-9]+)$', motiontypeViews.updatemotiontype, name='updatemotiontype'),

    #  定义处理修改运动类型的url地址响应方法，跳转到 motiontypeView的updatemotiontypeat方法
    url(r'^updatemotiontypeact/$', motiontypeViews.updatemotiontypeact, name='updatemotiontypeact'),

    #  定义跳转管理运动类型的url地址响应方法，跳转到 motiontypeView的motiontypemanage方法
    url(r'^motiontypemanage/$', motiontypeViews.motiontypemanage, name='motiontypemanage'),

    #  定义跳转查看运动类型的url地址响应方法，跳转到 motiontypeView的motiontypeview方法
    url(r'^motiontypeview/$', motiontypeViews.motiontypeview, name='motiontypeview'),

    #  定义处理删除运动类型的url地址响应方法，跳转到 motiontypeView的deletemotiontype方法
    url(r'^deletemotiontypeact/(?P<id>[0-9]+)$', motiontypeViews.deletemotiontypeact, name='deletemotiontypeact'),

    #  定义跳转搜索运动类型的url地址响应方法，跳转到 motiontypeView的searchmotiontype方法
    url(r'^searchmotiontype/$', motiontypeViews.searchmotiontype, name='searchmotiontype'),

    #  定义运动类型详情的url地址响应方法，跳转到 motiontypeView的motiontypedetails方法
    url(r'^motiontypedetails/(?P<id>[0-9]+)$', motiontypeViews.motiontypedetails, name='motiontypedetails'),

    #  定义添加运动类型方法，响应页面请求，跳转到motiontypeViews的useraddmotiontype方法
    url(r'^useraddmotiontype/$', motiontypeViews.useraddmotiontype, name='useraddmotiontype'),

    #  定义处理添加运动类型方法，响应页面请求，跳转到motiontypeViews的useraddmotiontypeact方法
    url(r'^useraddmotiontypeact/$', motiontypeViews.useraddmotiontypeact, name='useraddmotiontypeact'),

    #  定义跳转修改运动类型方法，响应页面请求，跳转到motiontypeViews的userupdatemotiontype方法
    url(r'^userupdatemotiontype/(?P<id>[0-9]+)$', motiontypeViews.userupdatemotiontype, name='userupdatemotiontype'),

    #  定义处理修改运动类型方法，响应页面请求，跳转到motiontypeViews的userupdatemotiontypeact方法
    url(r'^userupdatemotiontypeact/$', motiontypeViews.userupdatemotiontypeact, name='userupdatemotiontypeact'),

    #  定义跳转运动类型管理方法，响应页面请求，跳转到motiontypeViews的usermotiontypemanage方法
    url(r'^usermotiontypemanage/$', motiontypeViews.usermotiontypemanage, name='usermotiontypemanage'),

    #  定义处理删除运动类型方法，响应页面请求，跳转到motiontypeViews的userdeletemotiontype方法
    url(r'^userdeletemotiontypeact/(?P<id>[0-9]+)$', motiontypeViews.userdeletemotiontypeact,
        name='userdeletemotiontypeact'),
]
