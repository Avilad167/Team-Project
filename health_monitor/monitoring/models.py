from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(default=25.0)  # Default temperature value
    humidity = models.FloatField(default=50.0)     # Default humidity value
    heart_rate = models.FloatField(default=70.0)   # Default heart rate value
    motion_detected = models.BooleanField(default=False)  # Default motion_detected value
    sensor_value = models.CharField(max_length=255, default='')  # The value to represent sensor data

    def __str__(self):
        return f"Sensor Value: {self.sensor_value}, Temperature: {self.temperature}, Humidity: {self.humidity}, Heart Rate: {self.heart_rate}, Motion Detected: {self.motion_detected}, Timestamp: {self.timestamp}"
