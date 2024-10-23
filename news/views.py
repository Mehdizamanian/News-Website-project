from django.shortcuts import render ,get_object_or_404, redirect
from .models import News ,Comment
from .forms import CommentForm 
from django.contrib import messages
from django.db.models import Q

from django.views.generic import ListView ,DeleteView ,UpdateView , DetailView ,CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin




def news_list(request,*args, **kwargs):
  news=News.objects.filter(active=True).order_by('-created_time')

  if kwargs.get('author'):
    news=news.filter(author__username=kwargs['author'])

  if kwargs.get('date'):
    news=news.filter(created_time__icontains=kwargs['date'])


  if kwargs.get('category'):
    news=news.filter(category__title=kwargs['category'])

  if kwargs.get('tag'):
    news=news.filter(tag__title=kwargs['tag'])

  search=request.GET.get('q')
  if search:
    news=news.filter( Q(title__icontains=search) | Q(brif_description__icontains=search)|Q(description__icontains=search))


  context={'news':news}
  return render(request,'news/news-list.html',context)





def news_detail(request,num):
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





# Admin dashboard

class AdminPannel(UserPassesTestMixin,SuccessMessageMixin,ListView):
  model=News
  context_object_name='news'
  template_name='news/admin-news/admin.html'
  success_message = "welcome {{request.user}} as superuser"

  def test_func(self):
      return self.request.user.is_superuser

  # def get_queryset(self):
  #     news=News.objects.all()
  #     return {'news':news}


class AdminDetail(UserPassesTestMixin,DeleteView):
  model=News
  context_object_name='new'
  template_name='news/admin-news/admin-detail.html'

  def test_func(self):
      return self.request.user.is_superuser





class AdminUpadte(UserPassesTestMixin,SuccessMessageMixin,UpdateView):
  model=News
  fields='__all__'
  template_name='news/admin-news/admin-form.html'
  success_url=reverse_lazy('news:dashboard')
  success_message = "one new updated successfully "
  
  def test_func(self):
      return self.request.user.is_superuser


class AdminDelete(UserPassesTestMixin,SuccessMessageMixin,DeleteView):
  model=News
  fields='__all__'
  context_object_name='new'
  template_name='news/admin-news/admin-delete.html'
  success_url=reverse_lazy('news:dashboard')
  success_message = "delete was successfully "
  
  def test_func(self):
      return self.request.user.is_superuser



class AdminCreate(UserPassesTestMixin,SuccessMessageMixin,CreateView):
    model = News
    fields='__all__'
    template_name='news/admin-news/admin-form.html'
    success_url=reverse_lazy('news:dashboard')
    success_message = "new added successfuly "
    
    def test_func(self):
      return self.request.user.is_superuser


  
  


  
