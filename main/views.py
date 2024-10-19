from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib import messages
# Main view to load the home page (index.html)
def main(request):
    template = loader.get_template('index.html')  # Assuming you have an index.html template
    return HttpResponse(template.render({}, request))

# Send email view with CSRF bypass for testing (not recommended for production)
@csrf_exempt  # Bypass CSRF for testing (remove in production)
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"From: {name}\nEmail: {email}\n\n{message}"
        
        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # Sender email
                ['aliboughnim6@gmail.com'],  # Your email to receive messages
                fail_silently=False,
            )
            messages.success(request, "Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, "Failed to send email. Please try again.")
        
    return render(request, 'index.html')  # Reload the same page with message