from django.urls import path
from . import views

urlpatterns = [
    path('', views.bun_Home, name="home"),
    path('login/', views.user_login, name="user_login"),
    path('signup/', views.user_signup, name="user_signup"),
    path('logout/', views.user_logout, name="user_logout"),
    path('store/', views.bun_store, name="bun_store"),
]

