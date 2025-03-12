from django.contrib import admin
from .models import SensorData

# Register the SensorData model with the admin interface
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'sensor_value', 'temperature', 'humidity', 'heart_rate', 'motion_detected')
    search_fields = ('sensor_value',)
    list_filter = ('timestamp', 'motion_detected')

admin.site.register(SensorData, SensorDataAdmin)
