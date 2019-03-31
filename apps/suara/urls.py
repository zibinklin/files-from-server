from django.contrib import admin
from django.urls import path

from apps.suara import views

urlpatterns = [
    path('',views.TambahSuaraView.as_view()),
    path('save',views.SaveSuaraView.as_view()),
    
]