from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL, will call the index view
    path('submit-sensor-data/', views.submit_sensor_data, name='submit_sensor_data'),
]
