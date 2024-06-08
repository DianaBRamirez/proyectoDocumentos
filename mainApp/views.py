from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.


def home(request):

    return render(request, 'home.html')   