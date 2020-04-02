from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView
from .models import Video
from .forms import VideoForm

# Create your views here.

class Index(TemplateView):
    template_name = 'app/index.html'
    context_object_name = 'videofile'
    #lastvideo= Video.objects.last()
    #queryset= lastvideo.videofile
    queryset= 'pepito'
    
    