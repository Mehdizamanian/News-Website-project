from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def index(request):
  return render(request,'website/tech-index.html')


def contact(request):
  if request.method=="POST":
    form=ContactForm(request.POST)
    if form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        subject=form.cleaned_data['subject']
        phone=form.cleaned_data['phone']
        message=form.cleaned_data['message']
        c=Contact()
        c.name=name
        c.email=email
        c.phone=phone
        c.subject=subject
        c.message=message
        c.save()
        messages.success(request, "Your message sent successfully")
        return redirect('/')
    else: 
       messages.error(request,'message not sent , dont leave name and email and phone empty  ')


  return render(request,'website/tech-contact.html')



# Create your views here.
