
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('programmes/', views.programmes, name='programmes'),
    path('programmes/ielts/', views.ielts, name='ielts'),
    path('programmes/php/', views.php, name='php'),
    path('programmes/mcse/', views.mcse, name='mcse'),
    path('programmes/oracle/', views.oracle, name='oracle'),
    path('programmes/autocad/', views.autocad, name='autocad'),
    path('programmes/microsoft/', views.microsoft, name='microsoft'),
    path('programmes/ccna/', views.ccna, name='ccna'),
    path('programmes/primavera/', views.primavera, name='primavera'),
    path('programmes/sql/', views.sql, name='sql'),
    path('programmes/pmp/', views.pmp, name='pmp'),
    path('programmes/java/', views.java, name='java'),
    path('programmes/python/', views.python, name='python'),
    path('programmes/webdesign/', views.webdesign, name='webdesign'),
]
