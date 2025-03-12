from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', include('monitoring.urls')),  # Include the URLs from your monitoring app
]
