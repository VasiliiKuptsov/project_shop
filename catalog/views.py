from django.shortcuts import render
from django.http import HttpResponse





def home_page(request):
    return render(request,'catalog/home_page.html')


def adress_page(request):
    return render(request,'catalog/adress_page.html')



# Create your views here.
