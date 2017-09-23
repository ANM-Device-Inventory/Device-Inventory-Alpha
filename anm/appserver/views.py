from django.shortcuts import render

from .models import NIC,HD,CPU
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Insert API
def insert(request):
    return HttpResponse("This is the insert api")

#Update API
def update(request):
    return HttpResponse("This is the update api")

#Delete API
def delete(request):
    return HttpResponse("This is the delete api")