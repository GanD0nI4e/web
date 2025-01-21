from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serializer

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'price', 'author']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']