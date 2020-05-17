from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import datetime

from .models import Profile, Book, Review


# Create your views here.
def index(request):
    return render(request, 'login_form.html')

def login(request):
    if request.POST:
        user = authenticate(username='john', password='secret')
        if user is not None:
            return render(request, 'profile.html')
    return render(request, 'login_form.html')

def register(request):
    if request.POST:
        user = User.objects.create_user(
            username=request.POST['email'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password'])
        time = datetime.now()
        activity = f"{time} : {user.first_name} {user.last_name} created an account! ;;"
        Profile.objects.create(
            user=user, about_me=request.POST['about_me'], 
            activity=activity, activity_time=time)
        request.session['log_id'] = user.id
        return redirect('/')
    return render(request, 'login_form.html')

def add_book(request):
    if request.POST:'
        if request.POST['location'] == 'library':
            errors = Book.objects.validator(request.POST)
        elif request.POST['location'] == 'wishlist':

            pass
    return render(request, 'book_form.html')

def add_author(request):
    author_last = request.POST['author_last'].capitalize()
    author_first = request.POST['author_first'].capitalize()
    author = Author.objects.filter(author_last = author_last).filter(author_first = author_first)
    if author > 1:
        author = author[0]
    else:
        Author.objects.create()



def view_profile(request):
    if request.session['log_id']:
        user = User.objects.get(id = request.session['log_id'])
        friends = user.Profile.friends.all()
        if len(friends) > 5:
            friends = friends[:5]
        context = {
            "user" : user,
            "friends" : friends
        }

def view_library(request):
    if request.session['log_id']:
        user = User.objects.get(id=request.session['log_id'])
        library = user.my_library.all()
        if len(library) == 0:
            user_library = False
        else:
            user_library = True
        context= {
            "user" : user,
            "user_library" : user_library,
            "my_library" : library,
            "available_books" : Book.objects.exclude(owner = request.session['log_id'])
        }
        return render(request, 'my_library.html', context)