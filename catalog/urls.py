from django.urls import path
from catalog.views import printing


urlpatterns = [
    path('hello/', printing)
]