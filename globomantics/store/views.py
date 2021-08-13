from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi There.")


def detail(request):
    return HttpResponse("More detail.")


def electronics(request):
    return HttpResponse("Electronics View.")