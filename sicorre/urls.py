from django.contrib import admin
from django.urls import path
from Recursos_Humanos import views

urlpatterns = [
        path('Recursos_Humanos/',views.usuarios,name='usuarios'),
]

""" urlpattner =[ path("admin/", admin.site.urls), ]"""
