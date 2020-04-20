from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tratamientos/', Tratamientos.as_view(), name = 'Tratamientos'),
    path('sobremi/', Index.as_view(), name = 'sobremi'),
    path('blog/', EntradaBlog.as_view(), name = 'blog'),
    path('infotratamiento/<int:pk>', Infotratamiento.as_view(), name = 'infotratamiento'),
    path('infoblog/<int:pk>', Infoblog.as_view(), name= 'infoblog'),
    

]