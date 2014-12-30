from django.http import HttpResponse
from django.shortcuts import redirect, render

from goat.apps.lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_text = request.POST.get('new_item', '')
        Item.objects.create(text=new_text)
        return redirect('/lists/uberlist/')

    return render(request, 'lists/home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items': items})