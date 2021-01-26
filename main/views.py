from django.shortcuts import render, HttpResponse, redirect
from .models import Books

def homepage(request):
    return render(request, "books.html")
    
def books(request):
    books_list = Books.objects.all()
    return render(request, 'books.html', {"books_list": books_list})


def add_book(request):
    if request.method=='POST':
        title = request.POST['book_title']
        subtitle = request.POST['book_subtitle']
        description = request.POST['book_description']
        price = request.POST['book_price']
        genre = request.POST['book_genre']
        author = request.POST['book_author']
        year = request.POST['book_year']
        ins = NewBooks(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
        ins.save()

    return redirect(books)


def delete_book(request, id):
    bookid = NewBooks.objects.get(id=id)
    bookid.delete()
    return redirect(books)

def mark_book(request, id):
    bookid = NewBooks.objects.get(id=id)
    bookid.is_favorite = True
    bookid.save()
    return redirect(books)
