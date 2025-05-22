from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Data coming from external folder')


def render2(request):
    # return render(request, 'index.html')
    return render(request, 'bootstrap_check.html')
