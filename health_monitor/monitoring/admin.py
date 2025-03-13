from django.contrib import admin
from .models import Patient, SensorData

admin.site.register(Patient)
admin.site.register(SensorData)
