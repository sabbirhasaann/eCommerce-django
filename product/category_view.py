from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def category(request):
    """Caterogy View"""
    return render(request, "add_category.html")


def categories(request):
    """Categories"""
    return render(request, "category_list.html")


@csrf_exempt
def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return JsonResponse({"name": name})
