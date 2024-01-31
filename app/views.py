from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form=Resgistration(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html',{'success':'Registration successfull. Please Login'})
        else:
            error_message=form.errors.as_text()
            return render(request,'register.html',{'error':error_message})
    return render(request,'register.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/dashboard")
        else:
            return render(request,'login.html',{'error':'Invalid Email or Password, please try again.'})
    return render(request,'login.html')


@login_required
def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def videoCAll(request):
    return render(request,'videoCall.html',{'name':request.user.username})

@login_required
def user_logout(request):
    logout(request)
    return redirect("/login")

@login_required
def join_call(request):
    return render(request,'join_room.html')

@login_required
def join_room(request):
    if request.method=='POST':
        roomid=request.POST['roomID']
        return redirect("http://127.0.0.1:8000/videoCall/?roomID="+roomid)
    return render(request,'join_room.html')