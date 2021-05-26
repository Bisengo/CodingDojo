from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
import bcrypt
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'regLoginTemplate.html')

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
    return redirect("/quotes")

def logout(request):
    request.session.clear()
    return redirect("/")

def login(request):
    print(request.POST)
    loginValidationerrors = User.objects.loginValidator(request.POST)
    print(loginValidationerrors)
    if len(loginValidationerrors)>0:
        for key,value in loginValidationerrors.items():
            messages.error(request, value) 
        return redirect("/")
    
    user = User.objects.get(email = request.POST['email'])
    request.session['loggedinId'] = user.id
    return redirect("/quotes")

def quotes(request):
    allQuotes = Quote.objects.all()
    print(allQuotes)
    context = {
        'quotesFromDB': allQuotes
    }
    return render(request, 'quoteTemplate.html', context)

def create(request):
    quoteValidationErrors = Quote.objects.quoteValidator(self, request.POST)
    if len(quoteValidationErrors)> 0:
        for key, value in quoteValidationErrors.items():
            messages.error(request, value)
        return redirect("/quotes/addquote")

    loggedinuser = request.session['loggedinId']
    newQuote = Quote.objects.create(author=request.POST['authorFromHtml'], content = request.POST['contentFromHtml'], uploader = loggedinuser)
    return redirect('/quotes')

