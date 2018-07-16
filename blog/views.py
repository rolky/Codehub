from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})


def categories(request):
    return render(request, 'blog/categories.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def signup(request):
    return render(request, 'blog/signup.html', {})

def login(request):
    return render(request, 'blog/login.html', {}) 
