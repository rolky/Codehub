from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:pk>', views.DetailView.as_view(), name="details"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('categories/', views.categories, name="categories"),
    path('signup/', views.signup, name="signup"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('login/', views.auth_login, name="login"),
    path('auth/', views.auth, name="auth"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('edit/', views.edit, name="edit"),
    path('logout/', views.auth_logout, name="logout"),
]