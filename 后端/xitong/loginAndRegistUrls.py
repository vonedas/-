# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import loginAndRegistViews

urlpatterns = [
                  # 登录相关
                  url(r'^login/$', loginAndRegistViews.login, name='login'),
                  url(r'^loginact/', loginAndRegistViews.loginact, name='loginact'),
                  url(r'^loginactjson/', loginAndRegistViews.loginactjson, name='loginactjson'),

                  # 注册相关
                  url(r'^regist/$', loginAndRegistViews.regist, name='regist'),
                  url(r'^registact/$', loginAndRegistViews.registact, name='registact'),
                  url(r'^registactjson/', loginAndRegistViews.registactjson, name='registactjson'),

                  # 退出系统
                  url(r'^tuichuxitong/$', loginAndRegistViews.tuichuxitong, name='tuichuxitong'),

                  # 管理员相关
                  url(r'^adminindex/$', loginAndRegistViews.adminindex, name='adminindex'),
                  url(r'^adminupdategerenxinxiact/$', loginAndRegistViews.adminupdategerenxinxiact,
                      name='adminupdategerenxinxiact'),

                  # 用户相关
                  url(r'^userindex/$', loginAndRegistViews.userindex, name='userindex'),
                  url(r'^userupdategerenxinxiact/$', loginAndRegistViews.userupdategerenxinxiact,
                      name='userupdategerenxinxiact'),

                  # AI医生
                  url(r'^aidoctor/$', loginAndRegistViews.aidoctor, name='aidoctor'),

                  # 分析功能
                  url(r'^analyzeVideo/', loginAndRegistViews.analyzeVideo, name='analyzeVideo'),
                  url(r'^analyzeFood/', loginAndRegistViews.analyzeFood, name='analyzeFood'),

                  # 用户管理相关
                  url(r'^getElderList/', loginAndRegistViews.getElderList, name='getElderList'),
                  url(r'^bindElder/', loginAndRegistViews.bindElder, name='bindElder'),
                  url(r'^getElderInfo/', loginAndRegistViews.getElderInfo, name='getElderInfo'),

                  # 健康数据相关
                  url(r'^getLatestBloodPressure/', loginAndRegistViews.getLatestBloodPressure,
                      name='getLatestBloodPressure'),
                  url(r'^getLatestWeight/', loginAndRegistViews.getLatestWeight, name='getLatestWeight'),
                  url(r'^getDietRecords/', loginAndRegistViews.getDietRecords, name='getDietRecords'),
                  url(r'^getExerciseRecords/', loginAndRegistViews.getExerciseRecords, name='getExerciseRecords'),
                  url(r'^getMedicineRecords/', loginAndRegistViews.getMedicineRecords, name='getMedicineRecords'),

                  url(r'^analyzeHealthData/', loginAndRegistViews.analyzeHealthData, name='analyzeHealthData'),

                  # 富文本编辑器图片上传
                  url(r'^upload/image/$', loginAndRegistViews.upload_image, name='upload_image'),

                  url('muteUser/(?P<id>[0-9]+)$', loginAndRegistViews.muteUser, name='muteUser'),
                  url('banUser/(?P<id>[0-9]+)$', loginAndRegistViews.banUser, name='banUser'),
                  url('restoreUser/(?P<id>[0-9]+)$', loginAndRegistViews.restoreUser, name='restoreUser'),

                  # 可视化数据接口
                    url(r'^keshihua/$', loginAndRegistViews.keshihua, name='keshihua'),
                  url(r'^getArticleCategories/$', loginAndRegistViews.getArticleCategories, name='getArticleCategories'),
                  url(r'^getUserStatus/$', loginAndRegistViews.getUserStatus, name='getUserStatus'),
                  url(r'^getHealthTrend/$', loginAndRegistViews.getHealthTrend, name='getHealthTrend'),

                    url('analyzeImage', loginAndRegistViews.analyzeImage, name='analyzeImage'),
                    url('getRankingData', loginAndRegistViews.getRankingData, name='getRankingData'),

                    url('getVerificationCode', loginAndRegistViews.getVerificationCode, name='getVerificationCode'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
