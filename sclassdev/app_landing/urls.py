from django.urls import path
from app_landing.views import view

urlpatterns = [
    path('', view, name='app-landing')
]

