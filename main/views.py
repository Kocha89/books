from django.shortcuts import render, HttpResponse
from .models import Books

def homepage(request):
    return render(request, "test.html")

def test(request):
    books_list = Books.objects.all()
    return render(request, 'test.html', {"books_list": books_list})


def add_book(request):
    form = request.POST
    title = form['book_title']
    subtitle = form['book_subtitle']
    description = form['book_description']
    price = form['book_price']
    genre = form['book_genre']
    author = form['book_author']
    year = form['book_year']