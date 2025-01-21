from django.db import models


class ItemManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name



class BookQuerySet(models.QuerySet):
    def by_author(self, author_id):
        return self.filter(author_id=author_id)

    def expensive_books(self, min_price):
        return self.filter(price__gte=min_price)


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = BookQuerySet.as_manager()