from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, World. You are at Chai aur Django About Page ")

def contact(request):
    return HttpResponse("Hello, World. You are at Chai aur Django Contact Page ")