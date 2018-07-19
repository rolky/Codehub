from django.shortcuts import render, get_object_or_404
from.models import Post, Category
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.views import generic

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/details.html'

# class IndexView(generic.ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'posts'

#     def get_queryset(self):
#         """Return the last five publication"""
#         return Post.objects.order_by('-published_date')[:5]

# Create your views here.

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-published_date')[:5]
    return render(request, 'blog/index.html',{ 'categories': categories, 'posts': posts })

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'blog/dashboard.html')
    else:
       return HttpResponseRedirect(reverse('blog:index')) 
        


def create(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        return render(request, 'blog/create.html', {'categories':categories})
    else:
       return HttpResponseRedirect(reverse('blog:index'))


def savepost(request):
    if request.user.is_authenticated:
        user = request.user
        category = Category(pk=request.POST['category'])
        title = request.POST['title']
        text = request.POST['text']
        post = Post(user=user, category=category, title=title, text=text)
        post.save()
    return HttpResponseRedirect(reverse('blog:index'))
       



def edit(request):
    return render(request, 'blog/edit.html', {})
    
# def details(request):
#     return render(request, 'blog/details.html',{})

def categories(request, id):
    category = get_object_or_404(Category, pk=id)
    posts = category.post_set.all().order_by('-published_date')
    return render(request, 'blog/categories.html', {'posts':posts})

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
    return HttpResponseRedirect(reverse('blog:auth_login'))

def auth_login(request):
    return render(request, 'blog/signin.html', {})

def auth(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return HttpResponseRedirect(reverse('blog:dashboard'))
        else:
            # No backend authenticated the credentials
            return HttpResponseRedirect(reverse('blog:index'))

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))
