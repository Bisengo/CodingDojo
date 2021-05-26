from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
    if "totalGold" not in request.session:
        request.session["totalGold"] = 0
    if "activities" not in request.session:
        request.session["activities"] = []
    return render(request, "index.html")

def process(request):
    #print(request.POST)
    #print(request.POST["location"])
    timeearned = datetime.datetime.now()
    print(timeearned)
    #process actions for Farm
    if request.POST["location"] == "Farm":
        # do logic for Farm
        earned = random.randint(10,20)
        print("*"*80)
        print(earned)
        print("*"*80)
        request.session["totalGold"] += earned
        activitystring = f"Earned {earned} golds in Farm {timeearned}"
        request.session["activities"].append(activitystring)

    #process actions for Cave
    elif request.POST["location"] == "Cave":
        # do logic for Cave
        earned = random.randint(5,10)
        print("*"*80)
        print(earned)
        print("*"*80)
        request.session["totalGold"] += earned
        activitystring = f"Earned {earned} golds in Cave {timeearned}"
        request.session["activities"].append(activitystring)

    #process actions for Cave
    elif request.POST["location"] == "House":
        # do logic for farm
        earned = random.randint(2,5)
        print("*"*80)
        print(earned)
        print("*"*80)
        request.session["totalGold"] += earned
        activitystring = f"Earned {earned} golds in House {timeearned}"
        request.session["activities"].append(activitystring)

    #process actions for Casino
    elif request.POST["location"] == "Casino":
        earned = random.randint(-50,50)
        print("*"*80)
        print(earned)
        print("*"*80)
        request.session["totalGold"] += earned

        if earned >= 0:
            activitystring = f"Earned {earned} golds in Casino {timeearned}"
        else:
            activitystring = f"Lost {earned} golds in Casino {timeearned}"
        request.session["activities"].append(activitystring)

    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")

def placeprocessing(request, place):
    timeearned = datetime.datetime.now()
    if place == "Farm":
        earned = random.randint(10, 20)
        request.session["totalGold"] += earned
        activitystring = f"Earned {earned} golds in Farm {timeearned}"
        request.session["activities"].append(activitystring)

    elif place == "Cave":
        earned = random.randint(5,10)
        request.session["totalGold"] += earned
        activitystring = f"Earned {earned} golds in Cave {timeearned}"
        request.session["activities"].append(activitystring)

    elif place == "House":
        earned = random.randint(2,5)
        request.session["totalGold"] += earned
        activitystring = f"Earned {earned} golds in House {timeearned}"
        request.session["activities"].append(activitystring)

    elif place == "Casino":
        earned = random.randint(-50,50)
        request.session["totalGold"] += earned
        if earned >= 0:
            activitystring = f"Earned {earned} golds in Casino {timeearned}"
        else:
            activitystring = f"Lost {earned} golds in Casino"
        request.session["activities"].append(activitystring)
    return redirect("/")





