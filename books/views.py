from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)


def book(request, pub_date):
    page = Book.objects.filter(pub_date=pub_date)

    try:
        books = Book.objects.all().order_by('-pub_date')
        preview = books.filter(pub_date__lt=pub_date)[:1].get()
        preview_page = preview.pub_date.strftime("%Y-%m-%d")
    except ObjectDoesNotExist:
        preview_page = None

    try:
        books = Book.objects.all().order_by('pub_date')
        nxt = books.filter(pub_date__gt=pub_date)[:1].get()
        next_page = nxt.pub_date.strftime("%Y-%m-%d")
    except ObjectDoesNotExist:
        next_page = None

    template = 'books/books_list.html'
    context = {'books': page, 'preview': preview_page,
               'next': next_page}
    return render(request, template, context)
