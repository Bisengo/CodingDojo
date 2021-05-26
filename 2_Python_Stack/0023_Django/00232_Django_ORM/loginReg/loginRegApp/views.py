from django.shortcuts import render, redirect
from .models import User, Item
from django.contrib import messages
import bcrypt
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def registerUser(request):
    print(request.POST)
    validationErrors = User.objects.registrationValidator(request.POST)
    print(validationErrors)
    if len(validationErrors)> 0:
        for key, value in validationErrors.items():
            messages.error(request, value)
        return redirect("/")
    hashedPW = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(firstName = request.POST['fname'], lastName = request.POST['lname'], email = request.POST['email'], password = hashedPW)
    request.session['loggedinId'] = newuser.id
    return redirect("/home")

def home(request):
    if 'loggedinId' not in request.session:
        return redirect("/")
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    context = {
        'loggedinUser': loggedinuser,
        'mywishes': Item.objects.filter(Q(uploader = loggedinuser) | Q(favoritor = loggedinuser)),
        'notMywishes': Item.objects.exclude(Q(uploader = loggedinuser) | Q(favoritor = loggedinuser))
    }
    
    return render(request, "home.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")

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
    return redirect("/home")

def wishAdd(request):
    return render(request, "addwish.html")

def create(request):
    #handle form info such as validating form info and adding the item to database
    print(request.POST)
    #send the form info to validator in models
    validationErrors = Item.objects.validateItem(request.POST)
    if len(validationErrors)>0:
        for key,value in validationErrors.items():
            messages.error(request, value) 
        return redirect('/wishes/add')
    #get the logged in user object so we can assign the item's uploader to that user object
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    #create item in database if there are no validation errors
    newWish = Item.objects.create(name = request.POST['itemName'], uploader = loggedinuser)
    return redirect("/home")

def addToFav(request, itemId):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    item = Item.objects.get(id = itemId)
    item.favoritor.add(loggedinuser)
    return redirect("/home")

def removefromFav(request, itemId):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    item = Item.objects.get(id = itemId)
    item.favoritor.remove(loggedinuser)
    return redirect("/home")

def deleteItem(request, itemId):
    item = Item.objects.get(id = itemId)
    item.delete()
    return redirect("/home")

def showItem(request, itemId):
    context = {
        'itemToShow': Item.objects.get(id = itemId)
    }
    return render(request, "showItem.html", context)



