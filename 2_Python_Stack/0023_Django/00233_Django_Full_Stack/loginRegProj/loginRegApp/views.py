from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt
# from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registerUser(request):
    print(request.POST)
    regValidationErrors = User.objects.registrationValidator(request.POST)
    print(regValidationErrors)
    if len(regValidationErrors)> 0:
        for key, value in regValidationErrors.items():
            messages.error(request, value)
        return redirect("/")
    hashedPW = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(firstName = request.POST['fname'], lastName = request.POST['lname'], email = request.POST['email'], password = hashedPW)
    request.session['loggedinId'] = newuser.id
    return redirect("/home")

def home(request):
    if 'loggedinId' not in request.session:
        return redirect("/")

    context = {
        'loggedinId': User.objects.get(id = request.session['loggedinId'])
    }
    return render(request, 'home.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    print(request.POST)
    loginValidationErrors = User.objects.loginValidator(request.POST)
    print(loginValidationErrors)
    if len(loginValidationErrors)>0:
        for key,value in loginValidationErrors.items():
            messages.error(request, value) 
        return redirect("/")
    
    user = User.objects.get(email = request.POST['email'])
    request.session['loggedinId'] = user.id
    return redirect("/home")