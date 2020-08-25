from rest_framework import serializers
from .models import Category, Author, Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        allow_blank=True,
        max_length=30)
    editorial = serializers.CharField(
        required=True,
        allow_blank=True,
        max_length=30)
    category = serializers.CharField()
    author = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        name = validated_data['name']
        editorial = validated_data['editorial']
        author = Author.objects.get(pk=validated_data['author'])
        category = Category.objects.get(pk=validated_data['category'])

        return Book.objects.create(name=name, editorial=editorial,
                                   author=author, category=category)


class AuthorLastnameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    lastname = serializers.CharField(
        required=True,
        allow_blank=True,
        max_length=30)


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        allow_blank=True,
        max_length=30)
    lastname = serializers.CharField(
        required=True,
        allow_blank=True,
        max_length=30)
    age = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Author` instance, given the validated data.
        """
        return Author.objects.create(**validated_data)


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        allow_blank=True,
        max_length=30)

    def create(self, validated_data):
        """
        Create and return a new `Category` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)
