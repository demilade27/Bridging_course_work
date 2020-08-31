from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path


from django.contrib import admin

urlpatterns = [

    path('', include('blog.urls')),
    path('cv/', include('resume.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
