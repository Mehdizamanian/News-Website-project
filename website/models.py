from django.db import models

class Contact(models.Model):
  name=models.CharField(max_length=60)
  email=models.EmailField(max_length=254,blank=False,null=False)
  phone=models.IntegerField()
  subject=models.CharField(max_length=200)
  message=models.TextField()
  created_time=models.DateTimeField(auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.email
  

  class Meta:
    ordering=['-created_time']

