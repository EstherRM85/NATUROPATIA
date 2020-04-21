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
        context['tratamiento']= Tratamiento.objects.get(pk = self.kwargs.get('pk',None))
        return context
    
    
    
    
"""class SobreMi(ListView):
    model = Info
    template_name = 'app/sobremi.html'
    context_object_name= 'mi' 
    queryset = Info.objects.all()"""

class Blog(ListView):
    model =  EntradaBlog
    template_name = 'app/blog.html'
    context_object_name= 'blog' 
    queryset = EntradaBlog.objects.all()


class InfoBlog(DetailView):
    template_name = 'app/blog2.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        textoBlog = EntradaBlog.objects.all()
        listadoBlog = super(InfoBlog, self).get_context_data(**kwargs)
        contexto = {'blo':textoBlog}
        contexto['info'] = EntradaBlog.objects.get(pk = self.kwargs.get('pk',None))
        return contexto

""" 
def consultar_cliente(request):
    plantillaCons = 'applibro/consultarcliente.html'#CREO LA PLANTILLA CONSULTAR
    listadocliente = Cliente.objects.all()#objects.all GUARDA LO QUE ESTA EN LA TABLA CLIENTE
    listadolibro = Libro.objects.all()
    contexto = {'cli':listadocliente}#MANDA DATOS A MI TEMPLATE ATRAVES DEL CONTEXTO
    contexto['object_list'] = listadocliente #CREO UNA LISTA PARA QUE EL CONTEXTO ME LO ENVIE  """






"""     template_name = 'app/blog2.html'
    model =  EntradaBlog

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(InfoBlog, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['informacion'] = EntradaBlog.objects.get(pk = self.kwargs.get('pk',None))
        return context """


  
    
    
    