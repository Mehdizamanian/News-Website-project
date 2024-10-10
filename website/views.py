from django.shortcuts import render


def index(request):
  return render(request,'website/tech-index.html')

# Create your views here.
