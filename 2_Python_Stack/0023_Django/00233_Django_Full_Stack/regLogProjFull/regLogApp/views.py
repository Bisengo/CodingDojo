from django.shortcuts import render, redirect
from .models import User, Item
from django.contrib import messages
import bcrypt
from django.db.models import Q

# Create your views here.

# rendering registration and login forms in index.html template
def index(request):
    return render(request, 'index.html')

# validating register form info and adding user to database
def registerUser(request):
    print(request.POST)
    # sending form info to register validator in models
    regValidationErrors = User.objects.registrationValidator(request.POST)
    print(regValidationErrors)
    if len(regValidationErrors)> 0:
        for key, value in regValidationErrors.items():
            messages.error(request, value)
        return redirect("/")
    # creating user (User object) in database if there are no validation errors
    hashedPW = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(firstName = request.POST['fname'], lastName = request.POST['lname'], email = request.POST['email'], password = hashedPW)
    request.session['loggedinId'] = newuser.id
    return redirect("/home")

# rendering info from database in home.html template
def home(request):
    if 'loggedinId' not in request.session:
        return redirect("/")
    # retrieving the loggedinuser (a User object) from the database
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    # retrieving all the items (Item objects) from the database
    allitems = Item.objects.all()
    # printing these items
    # print(allitems)
    mywishes = Item.objects.filter(Q(uploader = loggedinuser) | Q(favoritor = loggedinuser))
    notmywishes = Item.objects.exclude(Q(uploader = loggedinuser) | Q(favoritor = loggedinuser))
    context = {
        'loggedinId': loggedinuser,
        'allitems': allitems,
        'mywishes': mywishes,
        'notmywishes': notmywishes
    }
    return render(request, 'home.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    print(request.POST)
    # sending form info to login validator in models
    loginValidationErrors = User.objects.loginValidator(request.POST)
    print(loginValidationErrors)
    if len(loginValidationErrors)>0:
        for key,value in loginValidationErrors.items():
            messages.error(request, value) 
        return redirect("/")
    # logging in
    user = User.objects.get(email = request.POST['email'])
    request.session['loggedinId'] = user.id
    return redirect("/home")

# rendering new wish in the addwish.html template
def wishAdd(request):
    return render(request, "addwish.html")

# validating new wish form info and adding the wished item to database
def create(request):
    print(request.POST)
    # send the form info to validator in models
    itemValidationErrors = Item.objects.itemValidator(request.POST)
    if len(itemValidationErrors)>0:
        for key,value in itemValidationErrors.items():
            messages.error(request, value) 
        return redirect('/wishes/add')
    
    # one to many relationship
    #=========================
    # linking the new wish to its uploader
    # the logged in user (User object) is the uploader of the new wish (object) being created
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    # creating item (Item object) in database if there are no validation errors
    newWish = Item.objects.create(name = request.POST['itemName'], uploader = loggedinuser)
    return redirect("/home")

def addToFav(request, itemId):
    # many to many relationship
    #=========================
    # identifying the user (User object) 
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    # identifying the item (Item object)
    item = Item.objects.get(id = itemId)
    # linking the item and its favoritor (user)
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