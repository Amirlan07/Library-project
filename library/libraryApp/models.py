from django.db import models

class books_table(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('authors_table', on_delete=models.PROTECT, null=True)
    genre = models.ForeignKey('genres_table', on_delete=models.PROTECT, null=True)
    description = models.TextField()

class login_table (models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class genres_table(models.Model):
    genre = models.CharField(max_length=150)

class user_table(models.Model):
    user_name = models.CharField(max_length=50)
    login_id = models.ForeignKey('login_table', on_delete=models.PROTECT, null=True)
    readed_books = models.ManyToManyField(books_table,related_name='readed', null=True)
    favorit_books = models.ManyToManyField(books_table, related_name='favorit', null=True)

class coment_table(models.Model):
    user_id = models.ForeignKey('user_table', on_delete=models.PROTECT, null=True)
    coment = models.TextField()
    book_coment = models.ForeignKey('books_table', on_delete=models.PROTECT, null=True)


class authors_table(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)

class reading_books_table(models.Model):
    book_id = models.ForeignKey('books_table', on_delete=models.PROTECT, null=False)
    user_id = models.ForeignKey('user_table', on_delete=models.PROTECT, null=False)
    current_page = models.IntegerField()