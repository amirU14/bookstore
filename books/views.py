from django.shortcuts import render

from django.views import generic


from .models import Books


class BookListView(generic.ListView):
    model = Books
    template_name = 'books/book_list_view.html'
    context_object_name = 'books'


class BookDetail(generic.DetailView):
    model = Books
    template_name = 'books/book_detail_view.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Books
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Books
    fields = ['title', 'description', 'price', 'author']
    template_name = 'books/book_update.html'

