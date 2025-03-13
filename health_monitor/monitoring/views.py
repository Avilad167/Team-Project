from django.shortcuts import render
from .models import SensorData

def dashboard(request):
    latest_data = SensorData.objects.last()  # Get the latest sensor data
    context = {
        'temperature': latest_data.temperature if latest_data else '--',
        'heart_rate': latest_data.heart_rate if latest_data else '--',
        'humidity': latest_data.humidity if latest_data else '--',
        'motion_detected': latest_data.motion_detected if latest_data else '--',
    }
    return render(request, 'monitoring/index.html', context)

def report(request):
    # This is a simple report page placeholder
    return render(request, 'monitoring/report.html')

def settings(request):
    # This is a simple settings page placeholder
    return render(request, 'monitoring/settings.html')
