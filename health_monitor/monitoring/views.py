from django.shortcuts import render
from .models import SensorData  # Import SensorData model

def dashboard(request):
    latest_data = SensorData.objects.last()  # Get the latest sensor data
    context = {
        'temperature': latest_data.temperature if latest_data else '--',
        'heart_rate': latest_data.heart_rate if latest_data else '--',
        'humidity': latest_data.humidity if latest_data else '--',
        'motion_detected': latest_data.motion_detected if latest_data else '--',
    }
    return render(request, 'monitoring/index.html', context)

