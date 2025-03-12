from django.contrib import admin
from .models import Person, SensorData

class SensorDataInline(admin.TabularInline):
    model = SensorData
    extra = 1  # Allows adding a new sensor data record inline

class PersonAdmin(admin.ModelAdmin):
    inlines = [SensorDataInline]

admin.site.register(Person, PersonAdmin)
admin.site.register(SensorData)
