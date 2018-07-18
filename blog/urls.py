from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
     path('details/<id>', views.details, name="details"),
    path('categories/', views.categories, name="categories"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create" ),
    path('edit', views.about, name="about"),

    
]