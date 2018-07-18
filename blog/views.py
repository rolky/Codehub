from django.shortcuts import render
from.models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all()[:10]

    
        
    return render(request, 'blog/index.html', {'posts' : posts})
    
def details(request):
    return render(request, 'blog/details.html',{})

def categories(request):
    return render(request, 'blog/categories.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def signup(request):
    return render(request, 'blog/signup.html', {})

def login(request):
    return render(request, 'blog/login.html', {}) 


def create(request):
   
    return render(request, 'blog/create.html', {})
    
def update(request):
    return render(request, 'blog/edit.html', {})  