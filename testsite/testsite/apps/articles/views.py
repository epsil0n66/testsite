from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, мир")

def test(request):
    return HttpResponse("не заходи")
# Create your views here.
