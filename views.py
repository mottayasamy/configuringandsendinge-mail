
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

# Function to send a simple email
def send_email(subject, message, recipient_list):
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

# View to display the form and trigger the email sending
def send_simple_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = ['22uit013@kamarajengg.edu.in']  # Replace with the recipient's email address
        
        # Call the email sending function
        send_email(subject, message, recipient_list)
        
        return HttpResponse('Email sent successfully using Office 365!')
    return render(request, 'myapp/send_email_form.html')
