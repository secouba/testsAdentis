from django.urls import include, path
from . import views # import views so we can use them in urls.

urlpatterns = [
    path('', views.index),
]