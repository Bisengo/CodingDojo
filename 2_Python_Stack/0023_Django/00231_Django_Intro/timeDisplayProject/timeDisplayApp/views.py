from django.shortcuts import render, HttpResponse
from datetime import datetime
from time import gmtime, strftime

def display(request):
    context = {
    "date": strftime('%b %d, %Y', gmtime()),
    "time": strftime('%I:%M %p', gmtime())
    }
    return render(request, 'displaytime.html', context)

def display_td(request):
    context = {
    "date": strftime('%b %d, %Y', gmtime()),
    "time": strftime('%I:%M %p', gmtime())
    }
    return render(request, 'displaytime.html', context)
