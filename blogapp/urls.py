from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("<int:blog_id>/", views.detail, name = "detail"),
    path("newone/", views.blogpost, name="newone"),
    path("contributor/", views.contributor, name="contributor"),
    path('newblog/', views.blogpost, name="newblog"),
]