# coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import articleViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  #  定义添加文章的url地址响应方法，跳转到 articleView的addarticle方法
                  url(r'^addarticle/$', articleViews.addarticle, name='addarticle'),

                  url(r'^likedjson/$', articleViews.likedjson, name='likedjson'),

                  url(r'^collectedjson/$', articleViews.collectedjson, name='collectedjson'),

                  #  定义处理添加文章的url地址响应方法，跳转到 articleView的addarticleact方法
                  url(r'^addarticleact/$', articleViews.addarticleact, name='addarticleact'),

                  url(r'^articledetailsjson/$', articleViews.articledetailsjson, name='articledetailsjson'),

                  url(r'^searcharticlejson/$', articleViews.searcharticlejson, name='searcharticlejson'),

                  #  定义跳转修改文章的url地址响应方法，跳转到 articleView的updatearticle方法
                  url(r'^updatearticle/(?P<id>[0-9]+)$', articleViews.updatearticle, name='updatearticle'),

                  #  定义处理修改文章的url地址响应方法，跳转到 articleView的updatearticleat方法
                  url(r'^updatearticleact/$', articleViews.updatearticleact, name='updatearticleact'),

                  #  定义跳转管理文章的url地址响应方法，跳转到 articleView的articlemanage方法
                  url(r'^articlemanage/$', articleViews.articlemanage, name='articlemanage'),

                  #  定义跳转查看文章的url地址响应方法，跳转到 articleView的articleview方法
                  url(r'^articleview/$', articleViews.articleview, name='articleview'),

                  #  定义处理删除文章的url地址响应方法，跳转到 articleView的deletearticle方法
                  url(r'^deletearticleact/(?P<id>[0-9]+)$', articleViews.deletearticleact, name='deletearticleact'),

                  #  定义跳转搜索文章的url地址响应方法，跳转到 articleView的searcharticle方法
                  url(r'^searcharticle/$', articleViews.searcharticle, name='searcharticle'),

                  #  定义文章详情的url地址响应方法，跳转到 articleView的articledetails方法
                  url(r'^articledetails/(?P<id>[0-9]+)$', articleViews.articledetails, name='articledetails'),
                  #  定义文章点赞方法

                  url(r'^likedjson/$', articleViews.likedjson, name='likedjson'),

                  #  定义文章收藏方法

                  url(r'^collectedjson/$', articleViews.collectedjson, name='collectedjson'),

                  url('upload/', articleViews.upload_image, name='upload_image'),

                  url(r'^searcharticlebytypejson/$', articleViews.searcharticlebytypejson,
                      name='searcharticlebytypejson'),

                  url(r'^updateclicknumjson/$', articleViews.updateclicknumjson, name='updateclicknumjson'),


                url(r'^recoArticle/(?P<id>[0-9]+)$', articleViews.recoArticle, name='recoArticle'),

                url(r'^unrecoArticle/(?P<id>[0-9]+)$', articleViews.unrecoArticle, name='unrecoArticle'),

                url('getRecommendedArticles/', articleViews.getRecommendedArticles, name='getRecommendedArticles'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
