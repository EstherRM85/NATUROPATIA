from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('sobremi/', Index.as_view(), name = 'sobremi'),
    path('tratamientos/', Tratamientos.as_view(), name = 'Tratamientos'),
    path('infotratamiento/<int:pk>', Infotratamiento.as_view(), name = 'infotratamiento'),
    path('blog/', Blog.as_view(), name = 'blog'),
    path('infoblog/<int:pk>', InfoBlog.as_view(), name= 'infoblog'),
    path('patologias/', Patologias.as_view(), name= 'patologias'),
    path('testimonios/', Opiniones.as_view(), name= 'testimonios'),

]