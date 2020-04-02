from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView
# Create your views here.

class Index(TemplateView):
    template_name = 'app/index.html'