from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from . import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls), # admin site
    path('', views.index, name = 'index'),
    path('test/', views.test, name = 'test')
]