from django.db import models
from django.contrib.auth import get_user_model



user=get_user_model()


class News(models.Model):
  title=models.CharField(max_length=250)
  brif_description=models.TextField()
  description=models.TextField()
  image=models.ImageField(upload_to='news/images/',default='news/images/1.png')
  created_time=models.DateField(auto_now=False, auto_now_add=True)
  updated_time=models.DateField(auto_now=True, auto_now_add=False)
  active=models.BooleanField(default=False)
  author=models.ForeignKey(user,on_delete=models.CASCADE,blank=False)
  # relations
  category=models.ManyToManyField("Category")
  # tags=
  # slug=

  def __str__(self) -> str:
    return self.title


  class Meta:
    ordering=['-created_time']
    verbose_name = 'New'
    verbose_name_plural = 'News'





class Category(models.Model):
  title=models.CharField(max_length=100)
  
  def __str__(self):
    return self.title
  



class Comment(models.Model):
  news=models.ForeignKey(News, on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  email=models.EmailField(max_length=254)
  message=models.TextField()
  active=models.BooleanField(default=False)
  created_time=models.DateField( auto_now_add=True)


  def __str__(self):
    return self.name


  class Meta:
    ordering=['-created_time',]

