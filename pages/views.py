from pages.models import Content
from django.http import HttpResponse
from django.shortcuts import render
from .models import Content

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    contents = Content.objects.all()
    args = {
        'contents': contents
    }
    return render(request, 'index.html', args)
