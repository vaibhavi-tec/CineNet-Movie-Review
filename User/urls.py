from django.urls import path

from . import views

urlpatterns = [
    path("User/", views.index, name="index"),
]