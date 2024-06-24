# ipo/views.py
from django.shortcuts import render

def ipo(request):
    return render(request, 'index.html')

def upcomming(request):
    return render(request, 'upcomming.html')
