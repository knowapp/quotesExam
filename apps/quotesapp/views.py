# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from .models import *
import re
import bcrypt
from django.utils import timezone
from django.contrib import messages

# Display home page

def index (request) :  
    return render(request, 'index.html')

def registration_login(request) :
    return render(request, 'index.html')

def registration(request) :
    error = False
    # context = {}
    print "in registration"

    if request.method == "POST":
        print request.POST

        returnVal = User.objects.registration(request.POST)
        if returnVal['user'] :
            request.session['logged_in_user'] = returnVal['user'].id
            print "logged in user: ",request.session['logged_in_user']
            return redirect('quotes:home')
        else :
            for error in returnVal['errors'] :
                print error
                messages.error(request,error['message'],extra_tags=error['extra_tags'])
            return redirect('quotes:registration_login')

def login (request):
    if request.method == "POST":
        returnVal = User.objects.login(request.POST)
        if returnVal['user']:
            request.session['logged_in_user'] = returnVal['user'].id
            if 'order_id' in request.session :
                order = Order.objects.get(pk=request.session['order_id'])
                order.user = returnVal['user']
            print "logged in user: ",request.session['logged_in_user']
            return redirect('quotes:home')
        else:
            for error in returnVal['errors'] :
                print error
                messages.error(request,error['message'],extra_tags=error['extra_tags'])
            return redirect('quotes:login_registration')

def logout (request) :
    del request.session['logged_in_user']
    return redirect('quotes:home')

def __isLoggedIn__(request):
    if 'logged_in_user' in request.session:
        user = User.objects.get(pk=int(request.session['logged_in_user']))
        return user
    else :
        return None


