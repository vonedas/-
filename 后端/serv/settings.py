import os

# ... 其他设置 ...

# 媒体文件配置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 确保开发环境中可以访问媒体文件
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    # 添加媒体文件的 URL 配置
    from django.conf.urls.static import static
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT) 