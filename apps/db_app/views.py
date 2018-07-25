# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import User

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'db_app/sign.html')

def registration(request):
    return render(request, 'db_app/index.html')

def register(request):
    result = User.objects.registration_validation(request.POST)
    return redirect ('/display')

def display(request):
    context = {
        'users' :User.objects.all()
    }
    return render(request, 'db_app/display.html', context)

def edit(request, user_id):
    context = {
        'users' :User.objects.get(id = user_id)
    }
    return render(request, 'db_app/edit.html', context)

# Create your views here.
