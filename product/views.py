from django.shortcuts import HttpResponse, redirect, render

# Create your views here.

dummy_product = [
    {
        "image":"product01.png",
        "name":"Product 01",
        "sale": -30,
        "label": "NEW",
        "category":"Laptop",
        "old_price":980,
        "new_price":990,
        "rating":5,
    },
    {
        "image":"product02.png",
        "name":"Product 02",
        "sale": -30,
        "label": "NEW",
        "category":"Computer",
        "old_price":980,
        "new_price":990,
        "rating":5,
    },
]



def product_list(request):
    """Product List Function"""
    print(dummy_product)
    return render(request, "product1.html", {
        "products": dummy_product,
    })

def add_product(request):
    """Add Product View"""
    return render(request, "add_product.html")

def added_product(request):
    if request.method == "POST":

        name = request.POST.get('name')
        image = request.POST.get('image')
        rating = request.POST.get('rating')
    return HttpResponse(f"{name} + {image} + {rating}")