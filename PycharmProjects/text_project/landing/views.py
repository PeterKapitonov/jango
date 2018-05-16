from django.shortcuts import render

def landing(reguest):
    return render(request,'landing/landing.html',locals())