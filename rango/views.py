from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return <a href="https://tango_with_django_project/">Vist Project</a> ("Rango says hey there partner!")

def about(request):
    return <a href="https://tango_with_django_project/about/">Vist More Info</a>("Rango says here is the about page.")
