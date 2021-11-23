from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"), # name will use in templates
  path("about", views.about, name="about"),
]