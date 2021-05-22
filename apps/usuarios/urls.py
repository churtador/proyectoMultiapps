from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="usuarios"),
    path("crear/", views.crear, name="crear"),
    path("login/", views.login, name="login"),
]