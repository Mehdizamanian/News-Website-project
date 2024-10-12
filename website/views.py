from django.shortcuts import render


def index(request):
  return render(request,'website/tech-index.html')


def contact(request):
  return render(request,'website/tech-contact.html')

# Create your views here.
