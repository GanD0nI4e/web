from django.db.models import Prefetch
from .models import Book, Author
from django.db import transaction

def get_books_with_authors():
    return Book.objects.select_related('author')


def get_authors_with_books():
    return Author.objects.prefetch_related(Prefetch('books'))


def create_book_with_author(book_data, author_data):
    with transaction.atomic():
        author = Author.objects.create(**author_data)
        book = Book.objects.create(author=author, **book_data)
    return book