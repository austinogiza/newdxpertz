
from django.contrib import admin
from django.urls import path, include
from dxpert import urls
from django.conf import settings
from django.conf.urls import handler500
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dxpert.urls')),
]
