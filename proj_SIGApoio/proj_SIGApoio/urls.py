
from django.contrib import admin
from django.urls import path, include
from app_SIGApoio import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('cad_local/',views.cad_local, name = "cad_local"),
    path('success_page/', views.success_page, name = "success_page"),
    path('admin/', admin.site.urls)
]

