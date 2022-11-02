from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"Sales_app/index.html")

def sales(request):
    return HttpResponse("sales route")

# Create your views here.
