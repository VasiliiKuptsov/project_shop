from django.shortcuts import render
from django.http import HttpResponse

def printing(request):
    return HttpResponse('                                            jhhgfffrjuhh')




def adress_page(request):
    return render(request,'catalog/adress_page.html')

def home_page(request):
    return render(request,'catalog/includes/home_page.html')



# Create your views here.
