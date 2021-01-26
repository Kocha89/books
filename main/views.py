from django.shortcuts import render, HttpResponse, redirect
from .models import Books

def homepage(request):
    return render(request, "books.html")
    
def newbooks(request):
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
        ins = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
        ins.save()

    return redirect(newbooks)


def delete_todo(request, id):
    todo = Books.objects.get(id=id)
    todo.delete()
    return redirect(newbooks)

def mark_todo(request, id):
    todo = Books.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(newbooks)