from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    about=About.objects.first()
    skill=Skills.objects.all()
    edu=Education.objects.all()
    exp=Experience.objects.all()
    port=portfolio.objects.all()
    ser=Service.objects.all()
    return render(request,'index.html',{'about':about,'skill':skill,'edu':edu,'exp':exp,'port':port,'ser':ser})
    