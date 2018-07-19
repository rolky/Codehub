from django.shortcuts import render
from.models import Post, Category
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from .forms import PostForm
# Create your views here.

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-published_date')[:10]
    return render(request, 'blog/index.html',{ 'categories': categories, 'posts': posts })

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/edit/')
    else:
        form = PostForm()
        return render(request, 'blog/create.html', {'form': form})


def edit(request):
    return render(request, 'blog/edit.html', {})
    
def details(request,pk):
    post_id = Post.objects.get(pk=pk)
  #  post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/details.html', {'post': post_id})

def categories(request):
    return render(request, 'blog/categories.html', {})

def about(request):
    return render(request, 'blog/about.html', {})


def signup(request):
    return render(request, 'blog/signup.html', {})

def saveuser(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password']);
        user.last_name = request.POST['lastname']
        user.first_name = request.POST['firstname']
        user.save()
    return HttpResponseRedirect(reverse('blog:index'))

def login(request):
    return render(request, 'blog/signin.html', {})

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
