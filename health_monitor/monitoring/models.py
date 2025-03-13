from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    # You can add more fields here as required

    def __str__(self):
        return self.name

class SensorData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField(null=True, blank=True)
    heart_rate = models.IntegerField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    motion_detected = models.BooleanField(default=False)

    def __str__(self):
        return f"Data for {self.patient.name} at {self.timestamp}"
