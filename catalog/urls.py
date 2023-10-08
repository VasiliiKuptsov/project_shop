from django.urls import path
from catalog.views import home_page, adress_page




urlpatterns = [

    path('', home_page),
<<<<<<< HEAD
    ]
=======
    path('/catalog1', adress_page),
]
>>>>>>> adf036dd93ace6e245ac09e2260a4af6bb9dbf8f
