# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import recordhealthViews

urlpatterns = [

    #  定义添加健康记录的url地址响应方法，跳转到 recordhealthView的addrecordhealth方法
    url(r'^addrecordhealth/$', recordhealthViews.addrecordhealth, name='addrecordhealth'),

    url(r'^getHealthRecordVisualizationData/$', recordhealthViews.getHealthRecordVisualizationData,
        name='getHealthRecordVisualizationData'),

    url(r'^deleterecordhealthjson/$', recordhealthViews.deleterecordhealthjson, name='deleterecordhealthjson'),

    url(r'^searchrecordhealthjson/$', recordhealthViews.searchrecordhealthjson, name='searchrecordhealthjson'),

    url(r'^recordhealthdetailsjson/$', recordhealthViews.recordhealthdetailsjson, name='recordhealthdetailsjson'),

    url(r'^getHealthRecords/$', recordhealthViews.getHealthRecords, name='getHealthRecords'),

    #  定义处理添加健康记录的url地址响应方法，跳转到 recordhealthView的addrecordhealthact方法
    url(r'^addrecordhealthact/$', recordhealthViews.addrecordhealthact, name='addrecordhealthact'),

    #  定义处理添加健康记录的url地址响应方法，跳转到 recordhealthView的addrecordhealthact方法
    url(r'^addrecordhealthactjson/$', recordhealthViews.addrecordhealthactjson, name='addrecordhealthactjson'),

    #  定义跳转修改健康记录的url地址响应方法，跳转到 recordhealthView的updaterecordhealth方法
    url(r'^updaterecordhealth/(?P<id>[0-9]+)$', recordhealthViews.updaterecordhealth, name='updaterecordhealth'),

    #  定义处理修改健康记录的url地址响应方法，跳转到 recordhealthView的updaterecordhealthat方法
    url(r'^updaterecordhealthact/$', recordhealthViews.updaterecordhealthact, name='updaterecordhealthact'),

    #  定义跳转管理健康记录的url地址响应方法，跳转到 recordhealthView的recordhealthmanage方法
    url(r'^recordhealthmanage/$', recordhealthViews.recordhealthmanage, name='recordhealthmanage'),

    #  定义跳转查看健康记录的url地址响应方法，跳转到 recordhealthView的recordhealthview方法
    url(r'^recordhealthview/$', recordhealthViews.recordhealthview, name='recordhealthview'),

    #  定义处理删除健康记录的url地址响应方法，跳转到 recordhealthView的deleterecordhealth方法
    url(r'^deleterecordhealthact/(?P<id>[0-9]+)$', recordhealthViews.deleterecordhealthact,
        name='deleterecordhealthact'),

    #  定义跳转搜索健康记录的url地址响应方法，跳转到 recordhealthView的searchrecordhealth方法
    url(r'^searchrecordhealth/$', recordhealthViews.searchrecordhealth, name='searchrecordhealth'),

    #  定义健康记录详情的url地址响应方法，跳转到 recordhealthView的recordhealthdetails方法
    url(r'^recordhealthdetails/(?P<id>[0-9]+)$', recordhealthViews.recordhealthdetails, name='recordhealthdetails'),

    #  定义添加健康记录方法，响应页面请求，跳转到recordhealthViews的useraddrecordhealth方法
    url(r'^useraddrecordhealth/$', recordhealthViews.useraddrecordhealth, name='useraddrecordhealth'),

    #  定义处理添加健康记录方法，响应页面请求，跳转到recordhealthViews的useraddrecordhealthact方法
    url(r'^useraddrecordhealthact/$', recordhealthViews.useraddrecordhealthact, name='useraddrecordhealthact'),

    #  定义跳转修改健康记录方法，响应页面请求，跳转到recordhealthViews的userupdaterecordhealth方法
    url(r'^userupdaterecordhealth/(?P<id>[0-9]+)$', recordhealthViews.userupdaterecordhealth,
        name='userupdaterecordhealth'),

    #  定义处理修改健康记录方法，响应页面请求，跳转到recordhealthViews的userupdaterecordhealthact方法
    url(r'^userupdaterecordhealthact/$', recordhealthViews.userupdaterecordhealthact, name='userupdaterecordhealthact'),

    #  定义跳转健康记录管理方法，响应页面请求，跳转到recordhealthViews的userrecordhealthmanage方法
    url(r'^userrecordhealthmanage/$', recordhealthViews.userrecordhealthmanage, name='userrecordhealthmanage'),

    #  定义处理删除健康记录方法，响应页面请求，跳转到recordhealthViews的userdeleterecordhealth方法
    url(r'^userdeleterecordhealthact/(?P<id>[0-9]+)$', recordhealthViews.userdeleterecordhealthact,
        name='userdeleterecordhealthact'),

    url(r'^getCaloriesTrendSimple/$', recordhealthViews.getCaloriesTrendSimple, name='getCaloriesTrendSimple'),

]
