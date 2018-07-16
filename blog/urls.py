from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('categories/', views.categories, name="categories"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('about/', views.about, name="about")
]