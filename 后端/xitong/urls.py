from django.urls import path
from . import views
from . import articleViews

urlpatterns = [
    # ... existing code ...

    # 食物图片分析接口
    path('analyzeFood/', views.analyzeFood, name='analyzeFood'),

    # 图片上传接口
    path('upload/image/', views.upload_image, name='upload_image'),

    # 文章上传接口
    path('article/upload/', articleViews.upload_image, name='upload_image'),

    # 图片分析接口
    path('aidoctor/analyzeImage', views.analyzeImage, name='analyzeImage'),

    # ... existing code ...
]
