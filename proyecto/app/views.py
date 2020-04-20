from django.shortcuts import render
from django.views.generic import *
from .models import Video, Tratamiento,Info,EntradaBlog
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
        context['mi']= Info.objects.all()
        return context

class Tratamientos(ListView):
    model = Tratamiento
    template_name = 'app/tratamientos.html'
    context_object_name= 'tra' 
    queryset = Tratamiento.objects.all()


class Infotratamiento(DetailView):
    template_name = 'app/infoTratamiento.html'
    model = Tratamiento

    def get_context_data(self,**kwargs):
        context=super(Infotratamiento, self).get_context_data(**kwargs)
        context['tratamiento']= Tratamiento.objects.get(pk = self.kwargs.get('pk',None))
        return context
    
    
    
    
"""class SobreMi(ListView):
    model = Info
    template_name = 'app/sobremi.html'
    context_object_name= 'mi' 
    queryset = Info.objects.all()"""

class EntradaBlog(ListView):
    model =  EntradaBlog
    template_name = 'app/blog.html'
    context_object_name= 'blog' 
    queryset = EntradaBlog.objects.all()


class Infoblog(DetailView):
    template_name = 'app/blog2.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Infoblog).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['informacion'] = EntradaBlog.objects.get(pk = self.kwargs.get('pk',None))
        return context



  
    
    
    