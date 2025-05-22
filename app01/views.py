from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Edge 01')


# def htmlPage(request):
#     render(request, '')

def page01(request):
    return HttpResponse('Class 01 running')
