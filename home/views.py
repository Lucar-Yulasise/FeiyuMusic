from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requsts):
    return render(requsts,'index.html')
