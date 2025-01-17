from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render (request,'home.html')

def signup(req):
    return render(req,'signup.html')

def save(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('home')
    return render (request,'signup.html')

def index(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'index.html')

def LogoutPage(request):
    logout(request)
    return redirect('index')