from django.contrib import admin
from django.urls import path
from accounts import views
from . import views

app_name = "accounts"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name="update"),
    path('guide/', views.guide, name='guide'),
    path('trash/', views.trash, name='trash'),
    path('mypage', views.mypage, name='mypage'),
    # 강서소식
    path('list/', views.list, name='list'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    #path('write/', views.write, name='write'), 
    path('write/', views.create, name='create'),
    path('save/', views.save, name='save'),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name='delete'),
]