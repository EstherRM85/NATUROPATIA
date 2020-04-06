from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tratamientos/', Tratamiento.as_view(), name = 'Tratamientos'),
]