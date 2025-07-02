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
            "isnew": True
        },
        "category": "Laptop",
        "price": {
            "new": 990,
            "old": 980
        },
        "rating": 5,
        "topselling": True
    },
    {
        "image": "product02.png",
        "name": "Product 02",
        "label": {
            "sale": "-20%",
            "isnew": False
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4,
        "topselling": True,
    },
    {
        "image": "product03.png",
        "name": "Product 03",
        "label": {
            "sale": "-20%",
            "isnew": True
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4,
        "topselling":True,
    },
    {
        "image": "product04.png",
        "name": "Product 04",
        "label": {
            "sale": "-20%",
            "isnew": False
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4,
        "topselling": False,
    },
    {
        "image": "product05.png",
        "name": "Product 05",
        "label": {
            "sale": "-20%",
            "isnew": True
        },
        "category": "Computer",
        "price": {
            "new": 850,
            "old": 900
        },
        "rating": 4,
        "topselling": False
    },

]

new_dummy_products = [product for product in dummy_products if product["label"]["isnew"]]
topselling_dummy_products = [product for product in dummy_products if product.get("topselling", False)]

def page01(request):
    return HttpResponse('Class 01 running')

def index(request):
    """Main html File"""
    return render(request, "index.html",
                  {
                    "products": new_dummy_products,
                    "topproducts": topselling_dummy_products,
                  })