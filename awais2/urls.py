from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('register/' , views.register),
    path('login/' , views.login),
]