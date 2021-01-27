from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.apihelp, name="help"),
    path('api-auth/', include('rest_framework.urls')),
    path('gamelist/', views.gameList, name="gamelist"),
	path('gamedetail/<str:pk>/', views.gameDetail, name="gamedetail"),
	path('gameadd/', views.gameAdd, name="gameadd"),
	path('gameupdate/<str:pk>/', views.gameUpdate, name="gameupdate"),
	path('gamedelete/<str:pk>/', views.gameDelete, name="gamedelete"),
]
