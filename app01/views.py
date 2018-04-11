from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def hall(request):
    return HttpResponse("hello world")