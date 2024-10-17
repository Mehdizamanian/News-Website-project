from django.db import models
from django.contrib.auth import get_user_model



user=get_user_model()


class News(models.Model):
  title=models.CharField(max_length=250)
  brif_description=models.TextField()
  description=models.TextField()
  # image=
  created_time=models.DateField(auto_now=False, auto_now_add=True)
  updated_time=models.DateField(auto_now=True, auto_now_add=False)
  active=models.BooleanField(default=False)
  author=models.ForeignKey(user,on_delete=models.CASCADE,blank=False)
  # relations
  # categories=
  # tags=
  # slug=

  def __str__(self) -> str:
    return self.title


  class Meta:
    ordering=['-created_time']
    verbose_name = 'New'
    verbose_name_plural = 'News'
  

# Create your models here.