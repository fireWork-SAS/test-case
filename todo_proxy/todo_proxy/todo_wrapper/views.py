from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("working")


def todo_get(request):
    return HttpResponse("Hello, world. You're at the polls index.")
