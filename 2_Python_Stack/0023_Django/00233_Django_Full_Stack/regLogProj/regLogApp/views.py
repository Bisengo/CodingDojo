from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

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
    return redirect("/success")

def success(request):
    if 'loggedinId' not in request.session:
        return redirect("/")

    context = {
        'loggedinId': User.objects.get(id = request.session['loggedinId'])
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    print(request.POST)
    validation_errors = User.objects.loginValidator(request.POST)
    print(validation_errors)
    if len(validation_errors)>0:
        for key,value in validation_errors.items():
            messages.error(request, value) 
        return redirect("/")
    
    user = User.objects.get(email = request.POST['email'])
    request.session['loggedinId'] = user.id
    return redirect("/success")

