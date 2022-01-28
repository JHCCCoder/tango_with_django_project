from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpResponse):
    return HttpResponse('Rango says hey there partner!"<a href="/rango/about/">About</a>')

def about(request: HttpResponse):
    return HttpResponse('Rango says here is the about page.<a href="/rango/">Index</a>')