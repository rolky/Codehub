from django.shortcuts import render
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
    return render(request, 'blog/create.html', {})

def edit(request):
    return render(request, 'blog/edit.html', {})
    
def details(request):
    return render(request, 'blog/details.html',{})

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
