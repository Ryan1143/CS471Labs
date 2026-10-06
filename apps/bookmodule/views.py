from django.shortcuts import render
from django.http import HttpResponse
from .models import Book



def index2(request, val1=0):  # add the view function (index2)
    return HttpResponse("value1 = " + str(val1))


def index(request):
    return render(request, 'bookmodule/index.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)


def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')


def links(request):
    return render(request, 'bookmodule/html5/links.html')


def formatting(request):
    return render(request, "bookmodule/html5/formatting.html")


def listing(request):
    return render(request, "bookmodule/html5/listing.html")


def tables(request):
    return render(request, "bookmodule/html5/tables.html")