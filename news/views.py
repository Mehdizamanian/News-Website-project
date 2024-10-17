from django.shortcuts import render


def NewsListView(request):
  return render(request,'news/news-list.html')

# Create your views here.
