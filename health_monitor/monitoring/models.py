from django.db import models

# Define the Person model
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Define the SensorData model
class SensorData(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)  # ForeignKey to Person
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(default=25.0)
    humidity = models.FloatField(default=50.0)
    heart_rate = models.FloatField(default=70.0)
    motion_detected = models.BooleanField(default=False)
    sensor_value = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"Person: {self.person.name}, Sensor Value: {self.sensor_value}, Temperature: {self.temperature}, Humidity: {self.humidity}, Heart Rate: {self.heart_rate}, Motion Detected: {self.motion_detected}, Timestamp: {self.timestamp}"
