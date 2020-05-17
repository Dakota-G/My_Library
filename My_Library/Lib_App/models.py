from django.db import models
from django.contrib.auth.models import User


class Book_Manager(models.Manager):
    errors = {}
    def validator(title, author):
        if len(title) == 0: 
            errors['title'] = "Please enter a book title!"
        books_db = Books.objects.filter('title' = title)
        if len(books_db) > 0:
            errors['title_dup'] = "That title already exists!"
        if len(author) == 0
            errors['author'] = "Please enter an author!"
        return errors

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=500)
    friends = models.ManyToManyField('self')
    activity = models.TextField(null=True)
    activity_time = models.DateTimeField(auto_now=True, null=True)
    # activity separated by ';;'

class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=25, null=True)
    pub_date = models.IntegerField(null=True)
    desc = models.TextField(max_length=500, null=True)
    owner = models.ManyToManyField(Profile, related_name="library")
    wished = models.ManyToManyField(Profile, related_name="wish_list")
    borrowed = models.ManyToManyField(Profile, related_name="borrowed_books")
    readers = models.ManyToManyField(Profile, related_name="reading")
    objects = Book_Manager()

class Author(models.Model):
    author_first = models.CharField(max_length=100)
    author_last = models.Charfield(max_length=100)
    books = models.ManyToManyField(Book, related_name="authors")

class Review(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    reviewer = models.ManyToManyField(Profile, related_name="reviews")
    recommended_for = models.ManyToManyField(Profile, related_name="recommendations")
    reviewed_book = models.ForeignKey(Book, related_name="review", on_delete=models.CASCADE)