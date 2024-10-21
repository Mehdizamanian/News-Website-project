from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required


def login_view(request):
  if request.method=="POST":
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request,username=username,password=password)
    if user:
      login(request,user)
      messages.success(request,'you logged in successfully   &nbsp;&nbsp; &nbsp;   ')
      return redirect('/')
  else:
    form=AuthenticationForm #username #password
  return render(request,'accounts/login.html',{'form':form})


@login_required
def logout_view(request):
  logout(request)
  messages.success(request,'you logged out &nbsp;    &nbsp;   ')
  return redirect('/')




def signupview(request):
  if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
      messages.success(request,'signup completed . </br> enter your username and password bellow . </br></br>')
      form.save()
      return redirect("accounts:login")
  else:    
    form=UserCreationForm
  return render(request,'accounts/signup.html',{'form':form})



# Create your views here.
