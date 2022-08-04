from unicodedata import *
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import  redirect, render
from django.db.models import *
from django.contrib.auth.models import Group
from django.contrib.auth import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')
        
def index1(request):
    return render(request, 'dashboard/index-1.html')        


