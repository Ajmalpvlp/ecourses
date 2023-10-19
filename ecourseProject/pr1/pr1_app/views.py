from .models import Member
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages  # Import messages module


# Create your views here.
def sregister(request):
    if request.method == 'POST':
        name= request.POST['name']  
        parent= request.POST['parent']
        adrs= request.POST['adrs']
        district= request.POST['district']
        # dob= request.POST['dob']
        tel= request.POST['tel']
        course= request.POST['course']
        newmember= Member.objects.create(name=name, parent=parent, adrs=adrs, district=district, tel=tel, course=course) 
        newmember.save()
        return redirect('showlist')
        # return render(request, 'showlist.html')
    return render(request, 'sregister.html')

def submited(request):
    return render(request, 'submited.html')

def update(request, id):
    obj = Member.objects.get(pk = id)

    if request.method == 'POST':
        
        try:
            name= request.POST['name']  
            parent= request.POST['parent']
            adrs= request.POST['adrs']
            district= request.POST['district']
            # dob= request.POST['dob']
            tel= request.POST['tel']
            course= request.POST['course']
            
            obj.name = name
            obj.parent = parent
            obj.adrs = adrs
            obj.district = district
            # obj.dob = dob
            obj.tel = tel
            obj.course = course
            obj.save()  
            return redirect('showlist')
        except:
            MultiValueDictKeyError
    return render(request, 'update.html', {'obj': obj})

def deletedata(request, id):
    if request.method == 'POST':
        dl = Member.objects.get(pk=id)
        dl.delete()
        return redirect('showlist')
    return render(request, 'index.html')

def showlist(request):
    mem = Member.objects.all()
    return render(request, 'showlist.html', {'mem': mem})

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def login1(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['loginpassword']
        loguser = authenticate(username=name, password=password)
        
        if loguser is not None:
            login(request, loguser)
            return HttpResponseRedirect('/sregister')
        else:
            return redirect ('/signup')
    return render(request, 'login.html' )

def logout1(request):
    logout(request)
    return render(request, 'index.html')
       
def signup(request):
    if request.method == 'POST':
        name = request.POST['signupname']
        mail = request.POST['signupmail']
        password = request.POST['signuppassword']
        newuser = User.objects.create_user(name, mail, password)
        newuser.save()
        return redirect('/login')
    return render(request, 'signup.html')