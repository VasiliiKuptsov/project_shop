from django.shortcuts import render
from django.http import HttpResponse


def printing(request):
    return HttpResponse('okey/')


def index_hello(request):
    return renger(request,'home_page.html')


def index_bay(request):
    return renger(request,'adress_page.html')



# Create your views here.
