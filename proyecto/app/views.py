from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import VideoForm

# Create your views here.

    
class Index(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        context=super(Index, self).get_context_data(**kwargs)
        listaVideos=Video.objects.all()
        if (len(listaVideos)>0): #Si hay videos
            lastvideo= Video.objects.all()[0]
            context['videofile']= lastvideo.videofile
            
        context['mi']= Inicio.objects.all()[0]
        context['contacto']= Contacto.objects.all()
        context['template']= 'app:index'
        
        return context

class Tratamientos(ListView):
    model = Tratamiento
    template_name = 'app/tratamientos.html'
    context_object_name= 'tra' 
    queryset = Tratamiento.objects.all()

    
    def get_context_data(self,**kwargs):
        context=super(Tratamientos, self).get_context_data(**kwargs)
        context['contacto']= Contacto.objects.all()
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:tratamientos'
        return context


class Infotratamiento(DetailView):
    template_name = 'app/infoTratamiento.html'
    model = Tratamiento

    def get_context_data(self,**kwargs):
        context=super(Infotratamiento, self).get_context_data(**kwargs)
        idTrat = self.kwargs.get('pk',None)
        context['trat']= Tratamiento.objects.get(pk = idTrat)
        context['contacto']= Contacto.objects.all()
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:infotratamiento'
        context['idTemp'] = idTrat
        return context

class Patologias(ListView):
    model = Patologia
    template_name = 'app/patologias.html'
    context_object_name= 'pat' 
    queryset = Patologia.objects.all()

    def get_context_data(self,**kwargs):
        context=super(Patologias, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('pk', None)
        context['Psis'] = Sistema.objects.all() 
        context['contacto']= Contacto.objects.all() 
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:patologias'        
        return context
    
    
class Blog(ListView):
    model =  EntradaBlog
    template_name = 'app/blog.html'
    paginate_by = 4
    context_object_name= 'blog' 
    queryset = EntradaBlog.objects.all()

    def get_context_data(self,**kwargs):
        context=super(Blog, self).get_context_data(**kwargs)
        context['destacados']= EntradaBlog.objects.filter(destacados = True)[:4]
        context['contacto']= Contacto.objects.all()
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:blog'  
        return context       


class InfoBlog(DetailView):
    template_name = 'app/infoBlog.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        context = super(InfoBlog, self).get_context_data(**kwargs)
        idblog = self.kwargs.get('pk',None)
        context['info'] = EntradaBlog.objects.get(pk = idblog)
        context['contacto']= Contacto.objects.all()
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:infoblog'
        context['idTemp'] = idblog
        return context


class Opiniones(ListView):
    model = Testimonio
    template_name = 'app/testimonios.html'
   
    def get_context_data(self, **kwargs):
        context=super(Opiniones, self).get_context_data(**kwargs)
        context['opi']= Testimonio.objects.all()
        context['contacto']= Contacto.objects.all()
        context['mi']= Inicio.objects.all()[0]
        context['template']= 'app:testimonios'
        return context
    



  
    
    
    