"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from xitong import adminViews,yinshiViews,userViews,tizhongViews,yaoViews,yinshilogViews,noticeViews,xueyaViews,duanlianlogViews,zinvViews,bangdingViews,loginAndRegistViews,motiontypeViews,healthrecordViews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	url(r'^login/',loginAndRegistViews.login, name='login'),
    # url(r'^healthrecord/',healthrecordViews.healthrecord, name='healthrecord'),

	url(r'^addfilejson/',loginAndRegistViews.addfilejson, name='addfilejson'),
    url(r'^loginAndRegist/', include('xitong.loginAndRegistUrls',namespace='loginAndRegist')),
    url(r'^loginactjson/',loginAndRegistViews.loginactjson, name='loginactjson'),
    url(r'^registactjson/',loginAndRegistViews.registactjson, name='registactjson'),
    url(r'^healthrecord/', include('xitong.healthrecordUrls',namespace='healthrecord')),
    url(r'^index/', include('xitong.indexUrls',namespace='index')),
    url(r'^admin/', include('xitong.adminUrls',namespace='admin')),
    url(r'^user/', include('xitong.userUrls',namespace='user')),
    url(r'^tizhong/', include('xitong.tizhongUrls',namespace='tizhong')),
    url(r'^yao/', include('xitong.yaoUrls',namespace='yao')),
    url(r'^yinshi/', include('xitong.yinshiUrls',namespace='yinshi')),
    url(r'^yinshilog/', include('xitong.yinshilogUrls',namespace='yinshilog')),
    url(r'^notice/', include('xitong.noticeUrls',namespace='notice')),
    url(r'^xueya/', include('xitong.xueyaUrls',namespace='xueya')),
    url(r'^zinv/', include('xitong.zinvUrls',namespace='zinv')),
    url(r'^motiontype/', include('xitong.motiontypeUrls',namespace='motiontype')),
    url(r'^recordhealth/', include('xitong.recordhealthUrls',namespace='recordhealth')),

    url(r'^articlecomment/', include('xitong.articlecommentUrls', namespace='articlecomment')),
    url(r'^article/', include('xitong.articleUrls', namespace='article')),
    url(r'^articletype/', include('xitong.articletypeUrls', namespace='articletype')),
    url(r'^liked/', include('xitong.likedUrls', namespace='liked')),
    url(r'^collected/', include('xitong.collectedUrls', namespace='collected')),

    url(r'^commentliked/', include('xitong.commentlikedUrls', namespace='commentliked')),
    url(r'^likedmessage/', include('xitong.likedmessageUrls', namespace='likedmessage')),




    url(r'^bangding/', include('xitong.bangdingUrls',namespace='bangding')),
    url(r'^duanlianlog/', include('xitong.duanlianlogUrls',namespace='duanlianlog')),
    url(r'^addadminactjson/',adminViews.addadminactjson, name='addadminactjson'),
    url(r'^updateadminactjson/',adminViews.updateadminactjson, name='updateadminactjson'),
    url(r'^deleteadminjson/',adminViews.deleteadminjson, name='deleteadminjson'),
    url(r'^searchadminjson/',adminViews.searchadminjson, name='searchadminjson'),
    url(r'^admindetailsjson/',adminViews.admindetailsjson, name='admindetailsjson'),
    url(r'^adduseractjson/',userViews.adduseractjson, name='adduseractjson'),
    url(r'^updateuseractjson/',userViews.updateuseractjson, name='updateuseractjson'),
    url(r'^deleteuserjson/',userViews.deleteuserjson, name='deleteuserjson'),
    url(r'^searchuserjson/',userViews.searchuserjson, name='searchuserjson'),
    url(r'^userdetailsjson/',userViews.userdetailsjson, name='userdetailsjson'),
    url(r'^addtizhongactjson/',tizhongViews.addtizhongactjson, name='addtizhongactjson'),
    url(r'^updatetizhongactjson/',tizhongViews.updatetizhongactjson, name='updatetizhongactjson'),
    url(r'^deletetizhongjson/',tizhongViews.deletetizhongjson, name='deletetizhongjson'),
    url(r'^searchtizhongjson/',tizhongViews.searchtizhongjson, name='searchtizhongjson'),
    url(r'^tizhongdetailsjson/',tizhongViews.tizhongdetailsjson, name='tizhongdetailsjson'),
    url(r'^addyaoactjson/',yaoViews.addyaoactjson, name='addyaoactjson'),
    url(r'^updateyaoactjson/',yaoViews.updateyaoactjson, name='updateyaoactjson'),
    url(r'^deleteyaojson/',yaoViews.deleteyaojson, name='deleteyaojson'),
    url(r'^searchyaojson/',yaoViews.searchyaojson, name='searchyaojson'),
    url(r'^yaodetailsjson/',yaoViews.yaodetailsjson, name='yaodetailsjson'),
    url(r'^addyinshiactjson/',yinshiViews.addyinshiactjson, name='addyinshiactjson'),
    url(r'^updateyinshiactjson/',yinshiViews.updateyinshiactjson, name='updateyinshiactjson'),
    url(r'^deleteyinshijson/',yinshiViews.deleteyinshijson, name='deleteyinshijson'),
    url(r'^searchyinshijson/',yinshiViews.searchyinshijson, name='searchyinshijson'),
    url(r'^yinshidetailsjson/',yinshiViews.yinshidetailsjson, name='yinshidetailsjson'),
    url(r'^addyinshilogactjson/',yinshilogViews.addyinshilogactjson, name='addyinshilogactjson'),
    url(r'^updateyinshilogactjson/',yinshilogViews.updateyinshilogactjson, name='updateyinshilogactjson'),
    url(r'^deleteyinshilogjson/',yinshilogViews.deleteyinshilogjson, name='deleteyinshilogjson'),
    url(r'^searchyinshilogjson/',yinshilogViews.searchyinshilogjson, name='searchyinshilogjson'),
    url(r'^yinshilogdetailsjson/',yinshilogViews.yinshilogdetailsjson, name='yinshilogdetailsjson'),
    url(r'^addnoticeactjson/',noticeViews.addnoticeactjson, name='addnoticeactjson'),
    url(r'^updatenoticeactjson/',noticeViews.updatenoticeactjson, name='updatenoticeactjson'),
    url(r'^deletenoticejson/',noticeViews.deletenoticejson, name='deletenoticejson'),
    url(r'^searchnoticejson/',noticeViews.searchnoticejson, name='searchnoticejson'),
    url(r'^noticedetailsjson/',noticeViews.noticedetailsjson, name='noticedetailsjson'),
    url(r'^addxueyaactjson/',xueyaViews.addxueyaactjson, name='addxueyaactjson'),
    url(r'^updatexueyaactjson/',xueyaViews.updatexueyaactjson, name='updatexueyaactjson'),
    url(r'^deletexueyajson/',xueyaViews.deletexueyajson, name='deletexueyajson'),
    url(r'^searchxueyajson/',xueyaViews.searchxueyajson, name='searchxueyajson'),
    url(r'^xueyadetailsjson/',xueyaViews.xueyadetailsjson, name='xueyadetailsjson'),
    url(r'^addduanlianlogactjson/',duanlianlogViews.addduanlianlogactjson, name='addduanlianlogactjson'),
    url(r'^updateduanlianlogactjson/',duanlianlogViews.updateduanlianlogactjson, name='updateduanlianlogactjson'),
    url(r'^deleteduanlianlogjson/',duanlianlogViews.deleteduanlianlogjson, name='deleteduanlianlogjson'),
    url(r'^searchduanlianlogjson/',duanlianlogViews.searchduanlianlogjson, name='searchduanlianlogjson'),
    url(r'^duanlianlogdetailsjson/',duanlianlogViews.duanlianlogdetailsjson, name='duanlianlogdetailsjson'),
    url(r'^addzinvactjson/', zinvViews.addzinvactjson, name='addzinvactjson'),
    url(r'^updatezinvactjson/', zinvViews.updatezinvactjson, name='updatezinvactjson'),
    url(r'^deletezinvjson/', zinvViews.deletezinvjson, name='deletezinvjson'),
    url(r'^searchzinvjson/', zinvViews.searchzinvjson, name='searchzinvjson'),
    url(r'^zinvdetailsjson/', zinvViews.zinvdetailsjson, name='zinvdetailsjson'),
    url(r'^addbangdingactjson/', bangdingViews.addbangdingactjson, name='addbangdingactjson'),
    url(r'^updatebangdingactjson/', bangdingViews.updatebangdingactjson, name='updatebangdingactjson'),
    url(r'^deletebangdingjson/', bangdingViews.deletebangdingjson, name='deletebangdingjson'),
    url(r'^searchbangdingjson/', bangdingViews.searchbangdingjson, name='searchbangdingjson'),
    url(r'^bangdingdetailsjson/', bangdingViews.bangdingdetailsjson, name='bangdingdetailsjson'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 在开发环境中启用媒体文件服务
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

