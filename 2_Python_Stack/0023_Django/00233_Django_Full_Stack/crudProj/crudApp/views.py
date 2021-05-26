from django.shortcuts import render, redirect
from .models import Birthday

# Create your views here.

def index(request):
    all_birthdays = Birthday.objects.all()
    context = {
        "all_bdays": all_birthdays
    }
    return render(request, "index.html", context)

def process_form(request):
    print("*"*50)
    print(request.POST)
    new_bday = Birthday.objects.create(
        value = request.POST["some_date"]
    )
    return redirect("/")

def edit_bday(request, bday_id):
    print(bday_id)
    context = {
        "bday_id": bday_id
    }
    return render(request, "edit.html", context)

def process_edit(request, bday_id):
    print(bday_id)
    print(request.POST)
    return redirect(f'/edit_bday/{bday_id}')