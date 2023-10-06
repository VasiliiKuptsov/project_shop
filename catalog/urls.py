from django.urls import path
from catalog.views import home_page, adress_page




urlpatterns = [
    path('', home_page),
    path('/catalog1', adress_page),
]