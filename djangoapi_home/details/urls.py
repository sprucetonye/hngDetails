
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    
    path('admin', admin.site.urls),
    path('profiles/', views.profile_list),
    re_path(r'^$', views.profile_list, name='profiles'),
]

