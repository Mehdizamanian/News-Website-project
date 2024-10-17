from django.shortcuts import render
from .models import News


def NewsListView(request,*args, **kwargs):
  news=News.objects.filter(active=True).order_by('-created_time')


  search=request.GET.get('q')
  if search:
    news=news.filter(title__icontains=search)


  context={'news':news}
  return render(request,'news/news-list.html',context)





def NewsDetailView(request,num):
  new=News.objects.get(id=num)
  return render(request,'news/news-detail.html',{'new':new})

# Create your views here.
