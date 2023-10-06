from django.urls import path
from catalog.views import home_page, adress_page




urlpatterns = [
<<<<<<< HEAD
    path('', home_page),
    path('/catalog1', adress_page),
=======
    path('', adress_page),
    path('', home_page),
>>>>>>> origin/main
]