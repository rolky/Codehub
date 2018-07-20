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
    posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')[:5]
    return render(request, 'blog/index.html', { 'categories': categories, 'posts': posts })

def dashboard(request):
    if request.user.is_authenticated:
        posts = request.user.post_set.all()
        return render(request, 'blog/dashboard.html', {'posts' : posts})
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
        category = int(request.POST['category'])
        user = User.objects.get(pk=request.user.id)
        title = request.POST['title']
        text = request.POST['text']
        post = Post(user=user, category=category, title=title, text=text)
        post.save()
    return HttpResponseRedirect(reverse('blog:dashboard'))
       



def edit(request, id):
    post = Post.objects.get(pk=id)
    categories = Category.objects.all()
    return render(request, 'blog/edit.html', {'post': post, 'categories': categories})
    

def updatepost(request, id):
    if request.user.is_authenticated:
        user = request.user
        post = Post.objects.get(pk=id)
        post.title = request.POST['title']
        post.text = request.POST['text']
        post.category = Category(pk=request.POST['category'])
        post.save()
    return HttpResponseRedirect(reverse('blog:dashboard'))

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
        user.is_staff=True
        user.save()
    return HttpResponseRedirect(reverse('blog:login'))

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

def deletepost(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('blog:dashboard'))
    
def publishpost(request, id):
    post = Post.objects.get(pk=id)
    post.publish()
    return HttpResponseRedirect(reverse('blog:dashboard'))