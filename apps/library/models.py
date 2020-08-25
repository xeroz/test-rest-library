from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Author(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()


class Book(models.Model):
    name = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE)
