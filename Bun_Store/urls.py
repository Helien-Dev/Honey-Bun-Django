from django.urls import path
from . import views

urlpatterns = [
    path('', views.bun_Home, name="home")
]
