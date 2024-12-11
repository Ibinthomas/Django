from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import *

# Create your views here.

def index(req):
    data=movie.objects.all()
    return render(req,'index.html',{'data':data})

def view_movie(req,id):
    data=movie.objects.get(pk=id)
    member=members.objects.filter(movie=data)
    return render(req,'page2.html',{'data':data, 'member':member})