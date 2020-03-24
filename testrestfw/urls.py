from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookapp.urls')),
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': settings.MEDIA_ROOT}),
]
