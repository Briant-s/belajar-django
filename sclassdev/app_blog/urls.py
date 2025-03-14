from django.urls import path
from .views import viewblog

urlpatterns = [
    path('', viewblog, name='app-blog')
]
