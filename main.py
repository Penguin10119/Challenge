from django.urls import path
from . import views

urlspatterns = [
    path("view", views.poll_view_function)
]