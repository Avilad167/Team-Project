from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-info-alert/', views.send_info_alert, name='send_info_alert'),

    path('', views.index, name='index'),  # Calls the index view to render vitals for multiple people
]
