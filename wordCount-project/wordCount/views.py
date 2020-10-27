from django.http import HttpResponse
from django.http import request
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    return render(request, "count.html")
