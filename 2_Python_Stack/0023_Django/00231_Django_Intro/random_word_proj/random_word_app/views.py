from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    rand_word = get_random_string(length=14)
    context = {
        "randomword": rand_word
    }
    return render(request, "randomword.html", context)

def generate(request):
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect('/')

