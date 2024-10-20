from django.shortcuts import render ,get_object_or_404, redirect
from .models import News ,Comment
from .forms import CommentForm

from django.contrib import messages



def NewsListView(request,*args, **kwargs):
  news=News.objects.filter(active=True)

  if kwargs.get('author'):
    news=news.filter(author__username=kwargs['author'])

  if kwargs.get('date'):
    news=news.filter(created_time__icontains=kwargs['date'])


  if kwargs.get('category'):
    news=news.filter(category__title=kwargs['category'])


  search=request.GET.get('q')
  if search:
    news=news.filter(title__icontains=search)


  context={'news':news}
  return render(request,'news/news-list.html',context)





def NewsDetailView(request,num):
  new=get_object_or_404(News,id=num)
  # new=News.objects.get(id=num)
  comments = Comment.objects.filter(news=new, active=True)

  form=CommentForm()

  if request.method =='POST':
    form=CommentForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "your comment added and would be published soon ... ")
      return redirect('/')

  return render(request,'news/news-detail.html',{'new':new , 'comments':comments ,'form':form})

# Create your views here.
