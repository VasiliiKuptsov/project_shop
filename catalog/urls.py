from django.urls import path
from catalog.views import home_page, adress_page




urlpatterns = [
    path('', home_page),
    path('', adress_page),
]