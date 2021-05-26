from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
import bcrypt

# Create your views here.

# index function rendering the reg & log forms
def index(request):
    return render(request, "index.html")

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
    # creating user (a User object) in database if there are no validation errors
    hashedPW = bcrypt.hashpw(request.POST['fpw'].encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(userName = request.POST['fname'], email = request.POST['femail'], password = hashedPW)
    request.session['loggedinId'] = newuser.id
    return redirect("/quotes")

def quotes(request):
    if 'loggedinId' not in request.session:
        return redirect("/")
    # retrieving the loggedinuser (a User object) from the database
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    # retrieving all the quotes (Quote objects) from the database
    allquotes = Quote.objects.all()
    # printing these quotes
    # print(allquotes)
    myfavquotes = Quote.objects.filter(favoritor = loggedinuser)
    notmyfavquotes = Quote.objects.exclude(favoritor = loggedinuser)
    context = {
        'loggedinId': loggedinuser,
        'allquotes': allquotes,
        'myfavquotes': myfavquotes,
        'notmyfavquotes': notmyfavquotes
    }
    return render(request, "quotes.html", context)

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
    user = User.objects.get(email = request.POST['femail'])
    request.session['loggedinId'] = user.id
    return redirect("/quotes")

# rendering new quote form in the addquote.html template
def contributeQuote(request):
    print(request.POST)
    # send the form info to validator in models
    quoteValidationErrors = Quote.objects.quoteValidator(request.POST)
    if len(quoteValidationErrors)>0:
        for key,value in quoteValidationErrors.items():
            messages.error(request, value) 
        return redirect('/quotes')
    # one to many relationship
    #=========================
    # linking the new quote to its uploader
    # the logged in user (User object) is the uploader of the new quote (Quote object) being created (contributed)
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    # creating a quote (Quote object) in database if there are no validation errors
    newQuote = Quote.objects.create(content = request.POST['fcontent'], author = request.POST['fauthor'], uploader = loggedinuser)
    return redirect("/quotes")

def addToFav(request, quoteId):
    # many to many relationship
    #=========================
    # identifying the user (User object) 
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    # identifying the quote (Quote object)
    quote = Quote.objects.get(id = quoteId)
    # linking the item and its favoritor (user)
    quote.favoritor.add(loggedinuser)
    return redirect("/quotes") 

def removefromFav(request, quoteId):
    loggedinuser = User.objects.get(id = request.session['loggedinId'])
    quote = Quote.objects.get(id = quoteId)        
    quote.favoritor.remove(loggedinuser)
    return redirect("/quotes")

# to render the template (quote form) to be edited
def showQuote(request, quoteId):
    quoteToEdit = Quote.objects.get(id=quoteId)
    print(quoteToEdit)
    context = {
        "quoteobj": quoteToEdit
    }
    return render(request, "editquote.html", context)


def edit(request, quoteId):
    print(request.POST)
    #send the form info to validator in models
    editquoteValidationErrors = Quote.objects.quoteValidator(request.POST)
    if len(editquoteValidationErrors)>0:
        for key,value in editquoteValidationErrors.items():
            messages.error(request, value) 
        return redirect(f'/quotes/{quoteId}')
        
    quoteobj = Quote.objects.get(id=quoteId)
    quoteobj.author = request.POST["fauthor"]
    quoteobj.content = request.POST["fcontent"]
    quoteobj.save()
    return redirect("/quotes")

def delete(request, quoteId):
    quoteobj = Quote.objects.get(id = quoteId)        
    quoteobj.delete()
    return redirect("/quotes")

def showusers(request, userId):
    poster = User.objects.get(id=userId)
    posts = Quote.objects.filter(uploader = poster)
    context = {
        'poster': poster,
        'posts' : posts,
        'count' : len(posts)
    }
    return render(request, "userpage.html", context)


