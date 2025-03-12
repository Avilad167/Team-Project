from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitoring.urls')),  # Add this line to map the root URL to the 'monitoring' app
]
