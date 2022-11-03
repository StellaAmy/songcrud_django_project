from django.shortcuts import render

# Create your views here.
def index(request):
    return Httpresponse('welcome to our site')