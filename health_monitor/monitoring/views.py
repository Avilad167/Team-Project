from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Assuming you have models for Person and SensorData, you may need to update as per your models
from .models import Person


@csrf_exempt
def send_info_alert(request):
    if request.method == 'POST':
        # Get the recipient email from the form
        recipient_email = request.POST.get('recipient_email')

        # Check if the email is provided
        if recipient_email:
            subject = "Health Monitoring Alert"
            message = "This is an alert message with the vital data or any other info you want."
            from_email = 'your_email@gmail.com'  # Replace with your email (use a real email address here)

            # Send email to the provided email address
            send_mail(subject, message, from_email, [recipient_email])

            return HttpResponse(f"Email sent successfully to {recipient_email}!")
        else:
            return HttpResponse("No email provided!")
    else:
        return HttpResponse("Invalid request method.")


def index(request):
    # Assuming 'persons' is your context variable
    persons = Person.objects.all()
    return render(request, 'index.html', {'persons': persons})
