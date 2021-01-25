from django.shortcuts import render, HttpResponse
from .models import Books

def homepage(request):
    return render(request, "test.html")

def test(request):
    books_list = Books.objects.all()
    return render(request, 'test.html', {"books_list": books_list})
