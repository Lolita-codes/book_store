from django.db.models import Avg
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.


def home(request):
    all_books = Book.objects.all()
    num_of_books = all_books.count()
    average_rating = all_books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {
        'books': all_books,
        'total_no_of_books': num_of_books,
        'average_rating': average_rating
    })


def book_detail(request, slug):
    # book = get_object_or_404(Book, pk=id)
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, 'book_outlet/book-details.html', {
        'book': book
    })
