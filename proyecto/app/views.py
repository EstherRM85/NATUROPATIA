from django.shortcuts import render
from django.views.generic import *
from .models import *
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
        context['trat']= Tratamiento.objects.get(pk = self.kwargs.get('pk',None))
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
        return context       


class InfoBlog(DetailView):
    template_name = 'app/infoBlog.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        context = super(InfoBlog, self).get_context_data(**kwargs)
        context['info'] = EntradaBlog.objects.get(pk = self.kwargs.get('pk',None))
        return context


  
    
    
    