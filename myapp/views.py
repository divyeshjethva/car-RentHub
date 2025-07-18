from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    avilables = AvailableCars.objects.all()
    trandings = TrendingOffers.objects.all()
    return render(request,'index.html',{'avilables':avilables,'trandings':trandings})

def register(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user:
                msg = "Email is Already Exists"
                return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                )
                msg = "Signup successfull"
                return render(request,'login.html',{'msg':msg})
            else:
                msg = "Passwor does not match"
                return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user.email == request.POST['email']:
                if user.password == request.POST['password']:
                    request.session['email'] = user.email
                    return redirect('index')
                else:
                    msg = "Password does not match"
                    return render(request,'login.html',{'msg':msg})
            else:
                msg = "Email is Not found"
                return render(request,'login.html',{'msg':msg})
        except:
            msg = "User is Not found"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def logout(request):
    del request.session['email']
    return redirect(login)

def contact(request):
    return render(request,'contact.html')
    
def about(request):
    return render(request,'about.html')
    
def cars(request):
    cars = Cars.objects.all()
    return render(request,'cars.html',{'cars':cars})
    
def blog(request):
    blog = Blog.objects.all()
    return render(request,'blog.html',{'blog':blog})