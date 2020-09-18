from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    title = 'Contact Form'
    message_form = None
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'MESSAGE FROM MY WEBSITE.COM'
            message = '%s %s' %(comment, name)
            emailFrom = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
            title = 'Thanks!'
            message_form = 'Thanks for message. We will get back to you!'
            form = None
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {
        'form': form,
        'title': title,
        'message_form': message_form,
    })
