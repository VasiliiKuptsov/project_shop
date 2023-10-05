from django.urls import path
from catalog.views import home_page, adress_page




urlpatterns = [
    path('', adress_page),
    path('', home_page),
]