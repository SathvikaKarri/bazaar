from django.shortcuts import render
from django.http import HttpResponse
from .models import item

# Create your views here.
def index(request):
    return render(request, "bazaar/index.html",
                  {"items": item.objects.all()})


def cart(request):
    return render(request, "bazaar/cart.html")