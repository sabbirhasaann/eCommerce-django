from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index1(request):
    return HttpResponse('Hello Edge 01')


# def htmlPage(request):
#     render(request, '')

dummy_products = [
    {
        "image": "product01.png",
        "name": "Product 01",
        "label": {
            "sale": "-30%",
            "isnew": "NEW"
        },
        "category": "Laptop",
        "price": {
            "new": 990,
            "old": 980
        },
        "rating": 5
    },
    {
        "image": "product02.png",
        "name": "Product 02",
        "label": {
            "sale": "-20%",
            "isnew": "NEW"
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4
    },
    {
        "image": "product03.png",
        "name": "Product 03",
        "label": {
            "sale": "-20%",
            "isnew": "NEW"
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4
    },
    {
        "image": "product04.png",
        "name": "Product 04",
        "label": {
            "sale": "-20%",
            "isnew": "NEW"
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4
    },
    {
        "image": "product05.png",
        "name": "Product 05",
        "label": {
            "sale": "-20%",
            "isnew": "NEW"
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4
    },

]

def page01(request):
    return HttpResponse('Class 01 running')

def index(request):
    """Main html File"""
    return render(request, "index.html", {"products": dummy_products})