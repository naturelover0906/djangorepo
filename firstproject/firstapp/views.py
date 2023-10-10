from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):  # the functin argument may be any name
    s='<h1> hello students , welcome to the classes of Mahesh sir for Django classes<h1>'
    return HttpResponse(s)



