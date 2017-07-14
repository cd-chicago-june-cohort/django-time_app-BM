# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime



def index(request):
    context = {
    "time": strftime("%A,  %b %d %Y at %H:%M:%S", localtime())
    }
    return render(request,'time_app/index.html', context)