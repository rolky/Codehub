from django.shortcuts import render
from.models import Post, Category
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'blog/jindex.html',{})

def details(request):
    return render(request, 'blog/details.html',{})


def categories(request):
    return render(request, 'blog/categories.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def signup(request):
    return render(request, 'blog/jsignup.html', {})

def saveuser(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password']);
        user.last_name = request.POST['lastname']
        user.first_name = request.POST['firstname']
        user.save()
    return HttpResponseRedirect(reverse('blog:index'))

def login(request):
    return render(request, 'blog/jlogin.html', {})

def auth(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
        else:
            # No backend authenticated the credentials
            pass   
    return HttpResponseRedirect(reverse('blog:index'))

def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))
