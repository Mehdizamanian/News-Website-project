from django.db import models
from django.utils import timezone

class Contact(models.Model):
  name=models.CharField(max_length=60)
  email=models.EmailField(max_length=254,blank=False,null=False)
  phone=models.IntegerField()
  subject=models.CharField(max_length=200)
  message=models.TextField()
  created_time=models.DateField(auto_now_add=False,default=timezone.now())

  def __str__(self):
    return self.email
  

  class Meta:
    ordering=['-created_time']

