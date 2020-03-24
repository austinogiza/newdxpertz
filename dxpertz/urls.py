
from django.contrib import admin
from django.urls import path, include
from dxpert import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dxpert.urls')),


]
