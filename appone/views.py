from django.shortcuts import render
from . models import *
from .forms import StudentForm,TeacherForm,SignupForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    data=Student.objects.all()
    return render(request,'index.html',{"data":data})

@login_required(login_url='login')
def addstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        address=request.POST['address']
        grade=request.POST['grade']
        new=Student(name=name,dob=dob,address=address,grade=grade)
        new.save()
        return redirect("home")
    form=StudentForm()
    return render(request,'addstudent.html',{"form":form})

@login_required(login_url='login')
def updatestudent(request,pk):
    form=Student.objects.get(id=pk)
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        address=request.POST['address']
        grade=request.POST['grade']

        form.name=name
        form.dob=dob
        form.address=address
        form.grade=grade

        form.save()
        return redirect('home')
    return render(request,'updatestudent.html',{'form':form})

@login_required(login_url='login')
def deletestudent(request,pk):
    form=Student.objects.get(id=pk)
    form.delete()
    return redirect("home")
    return render(request,'deletestudent.html')

@login_required(login_url='login')
def teacher(request):
    form=Teacher.objects.all()
    return render(request,'teacher.html',{'form':form})

@login_required(login_url='login')
def addteacher(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']

        new=Teacher(name=name,email=email,phone=phone,department=department)
        new.save()
        return redirect('teacher')
    form=TeacherForm
    return render(request,'addteacher.html',{'form':form})

@login_required(login_url='login')
def updateteacher(request,pk):
    form=Teacher.objects.get(id=pk)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']

        form.name=name
        form.email=email
        form.phone=phone
        form.department=department
        form.save()
        return redirect("teacher")
    return render(request,'updateteacher.html',{'form':form})

@login_required(login_url='login')
def deleteteacher(request,pk):
    new=Teacher.objects.get(id=pk)
    new.delete()
    return redirect('teacher')

def signup(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

        if User.objects.filter(email=email).exists():
            messages.info(request,"your Email Is Already Exists")
        elif password!=confirmpassword:
            messages.info(request,"Your Password And Confirm Password Are Not Same")
        else:
            create_user=User.objects.create_user(username,email,password)
            create_user.save()
            return redirect('login')
    form=SignupForm
    return render(request,'signup.html',{'form':form})
    
def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect("login")