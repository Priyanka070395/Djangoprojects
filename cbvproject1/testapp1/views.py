from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is child class of View</h1>')

class HelloWorldTemplateView(TemplateView):
    template_name='testapp1/results.html'

class HelloWorldTemplateContext(TemplateView):
    template_name='testapp1/info.html'
    def get_context_data(self, **kwargs): 
        context=super().get_context_data(**kwargs)
        context['name']='priya'
        context['subject']='maths'
        context['marks']=24
        return context
