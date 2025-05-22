"""CREATE UPDATE READ DELETE views"""
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Item
# Create
def create_item(request):
    """Create Item"""
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Item.objects.create(name=name, description=description) # pylint: disable=no-member
        return redirect('item_list')
    return render(request, 'create_item.html')

# Read
def item_list(request):
    """Item list"""
    items = Item.objects.all() # pylint: disable=no-member
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, id):
    """Item detail"""
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html', {'item': item})

# Update
def update_item(request, id):
    """Update Item"""
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('item_list')
    return render(request, 'update_item.html', {'item': item})


# Delete
def delete_item(request, id):
    """Delete item"""
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('item_list')
