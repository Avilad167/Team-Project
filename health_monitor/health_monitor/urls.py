from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('', include('monitoring.urls')),  # Includes URLs from the monitoring app
]
