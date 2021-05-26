from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def show(request):
    print(Show.objects.all)
    all_shows = Show.objects.all()
    context = {
        "all_shows": all_shows
    }
    return render(request, 'index.html', context)

def newForm(request):
    return render(request, "newform.html")


def process_form(request):
    print("*"*50)
    print(request.POST)
    new_show = Show.objects.create(title=request.POST["ftitle"], network=request.POST["fnetwork"], release_date=request.POST["frelease"], desc=request.POST["fdesc"])
    print(new_show)
    return redirect(f'/shows/{new_show.id}')

def showInfo(request, show_id):
    print(show_id)
    the_show = Show.objects.get(id=show_id)
    print(the_show)
    context = {
        "the_show": the_show
    }
    return render(request, "newShow.html", context)

# to render the template (form) to be edited
def editShow(request, show_id):
    showToEdit = Show.objects.get(id=show_id)
    print(showToEdit)
    context = {
        "showobj": showToEdit
    }
    return render(request, "editShowForm.html", context)

def updateShow(request, show_id):
    print(request.POST)
    showobj = Show.objects.get(id=show_id)
    showobj.title = request.POST["ftitle"]
    showobj.network = request.POST["fnetwork"]
    showobj.release_date = request.POST["frelease"]
    showobj.desc = request.POST["fdesc"]
    showobj.save()
    return redirect(f"/shows/{show_id}")

def delete(request, show_id):
    showobj = Show.objects.get(id=show_id)
    showobj.delete()
    return redirect('/shows')
