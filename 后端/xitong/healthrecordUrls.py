# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import healthrecordViews

urlpatterns = [

    #  定义添加健康记录类型的url地址响应方法，跳转到 healthrecordView的addhealthrecord方法
    url(r'^addhealthrecord/$', healthrecordViews.addhealthrecord, name='addhealthrecord'),

    #  定义处理添加健康记录类型的url地址响应方法，跳转到 healthrecordView的addhealthrecordact方法
    url(r'^addhealthrecordact/$', healthrecordViews.addhealthrecordact, name='addhealthrecordact'),

    url(r'^usersearchhealthrecordjson/$', healthrecordViews.usersearchhealthrecordjson, name='usersearchhealthrecordjson'),

    url(r'^deletehealthrecordjson/$', healthrecordViews.deletehealthrecordjson, name='deletehealthrecordjson'),

    url(r'^searchhealthrecordjson/$', healthrecordViews.searchhealthrecordjson, name='searchhealthrecordjson'),

    url(r'^addhealthrecordactjson/$', healthrecordViews.addhealthrecordactjson, name='addhealthrecordactjson'),

    #  定义跳转修改健康记录类型的url地址响应方法，跳转到 healthrecordView的updatehealthrecord方法
    url(r'^updatehealthrecord/(?P<id>[0-9]+)$', healthrecordViews.updatehealthrecord, name='updatehealthrecord'),

    #  定义处理修改健康记录类型的url地址响应方法，跳转到 healthrecordView的updatehealthrecordat方法
    url(r'^updatehealthrecordact/$', healthrecordViews.updatehealthrecordact, name='updatehealthrecordact'),

    #  定义跳转管理健康记录类型的url地址响应方法，跳转到 healthrecordView的healthrecordmanage方法
    url(r'^healthrecordmanage/$', healthrecordViews.healthrecordmanage, name='healthrecordmanage'),

    #  定义跳转查看健康记录类型的url地址响应方法，跳转到 healthrecordView的healthrecordview方法
    url(r'^healthrecordview/$', healthrecordViews.healthrecordview, name='healthrecordview'),

    #  定义处理删除健康记录类型的url地址响应方法，跳转到 healthrecordView的deletehealthrecord方法
    url(r'^deletehealthrecordact/(?P<id>[0-9]+)$', healthrecordViews.deletehealthrecordact,
        name='deletehealthrecordact'),

    #  定义跳转搜索健康记录类型的url地址响应方法，跳转到 healthrecordView的searchhealthrecord方法
    url(r'^searchhealthrecord/$', healthrecordViews.searchhealthrecord, name='searchhealthrecord'),

    #  定义健康记录类型详情的url地址响应方法，跳转到 healthrecordView的healthrecorddetails方法
    url(r'^healthrecorddetails/(?P<id>[0-9]+)$', healthrecordViews.healthrecorddetails, name='healthrecorddetails'),

    #  定义添加健康记录类型方法，响应页面请求，跳转到healthrecordViews的useraddhealthrecord方法
    url(r'^useraddhealthrecord/$', healthrecordViews.useraddhealthrecord, name='useraddhealthrecord'),

    #  定义处理添加健康记录类型方法，响应页面请求，跳转到healthrecordViews的useraddhealthrecordact方法
    url(r'^useraddhealthrecordact/$', healthrecordViews.useraddhealthrecordact, name='useraddhealthrecordact'),

    #  定义跳转修改健康记录类型方法，响应页面请求，跳转到healthrecordViews的userupdatehealthrecord方法
    url(r'^userupdatehealthrecord/(?P<id>[0-9]+)$', healthrecordViews.userupdatehealthrecord,
        name='userupdatehealthrecord'),

    #  定义处理修改健康记录类型方法，响应页面请求，跳转到healthrecordViews的userupdatehealthrecordact方法
    url(r'^userupdatehealthrecordact/$', healthrecordViews.userupdatehealthrecordact, name='userupdatehealthrecordact'),

    #  定义跳转健康记录类型管理方法，响应页面请求，跳转到healthrecordViews的userhealthrecordmanage方法
    url(r'^userhealthrecordmanage/$', healthrecordViews.userhealthrecordmanage, name='userhealthrecordmanage'),

    #  定义处理删除健康记录类型方法，响应页面请求，跳转到healthrecordViews的userdeletehealthrecord方法
    url(r'^userdeletehealthrecordact/(?P<id>[0-9]+)$', healthrecordViews.userdeletehealthrecordact,
        name='userdeletehealthrecordact'),
]
