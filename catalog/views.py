from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_genre = Genre.objects.all().count()
    num_books_containing_of = Book.objects.filter(title__icontains='of').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_books_containing_of': num_books_containing_of,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

def AuthorDetailView(request, pk):
    author = Author.objects.get(pk=pk)
    books_of_author = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books_of_author': books_of_author,
    }
    return render(request, 'catalog/author_detail.html', context=context)