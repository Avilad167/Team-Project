from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard page
    path('report/', views.report, name='report'),  # Report page
    path('settings/', views.settings, name='settings'),  # Settings page
]
