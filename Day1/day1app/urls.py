from django.urls import path
from day1app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newpage", views.newpage, name ="newpage"),
    path("add", views.result, name ="result")
]