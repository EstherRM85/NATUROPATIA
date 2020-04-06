from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView
from .models import Video, Tratamiento
from .forms import VideoForm

# Create your views here.

    
class Index(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        context_object_name = 'videofile'
        #context['videofile']=Video.objects.all()
        lastvideo= Video.objects.all()[0]
        context['videofile']= lastvideo.videofile
        return context

class Tratamiento(ListView):
    model = Tratamiento
    template_name = 'app/tratamientos.html'
    context_object_name= 'tra' 
    queryset = Tratamiento.objects.all()
    
    