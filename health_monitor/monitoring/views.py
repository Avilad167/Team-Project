from django.shortcuts import render
from .models import SensorData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Index view to render the template and display sensor data
def index(request):
    # Retrieve all sensor data and order by timestamp (most recent first)
    data = SensorData.objects.all().order_by('-timestamp')
    return render(request, 'monitoring/index.html', {'data': data})

# Handle sensor data submission via AJAX (this view will be used for POST requests)
@csrf_exempt  # Disable CSRF validation for this view (use CSRF tokens in production)
def submit_sensor_data(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data sent by AJAX
            data = json.loads(request.body)
            sensor_value = data.get('sensorValue')  # Get the sensor value from the request

            # Ensure sensor value is provided
            if not sensor_value:
                return JsonResponse({'error': 'Sensor value is required!'}, status=400)

            # Save the sensor value to the database
            new_data = SensorData(sensor_value=sensor_value)  # Use the correct field name 'sensor_value'
            new_data.save()

            # Return success message
            return JsonResponse({'message': 'Sensor data received and saved successfully!', 'sensorValue': sensor_value})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    # Handle cases when the method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=405)
