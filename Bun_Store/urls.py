from django.urls import path
from . import views

urlpatterns = [
    path('', views.bun_Home, name="home"),
    path('login/', views.user_login, name="user_login"),
    path('signup/', views.user_signup, name="user_signup"),
    path('logout/', views.user_logout, name="user_logout"),
    path('store/', views.bun_store, name="bun_store"),
    path('cart/', views.bun_cart, name="bun_cart"),
    path('checkout/', views.bun_checkout, name="bun_checkout"),
    path('update_item/', views.bun_updateItem, name="bun_updateItem"),
    path('process_order/', views.bun_processOrder, name="bun_processOrder"),
    path('pagina/<slug:slug>/', views.detalle_pagina, name='detalle_pagina'),
]

