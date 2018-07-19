from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:pk>', views.DetailView.as_view(), name="details"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('categories/<int:id>', views.categories, name="categories"),
    path('signup/', views.signup, name="signup"),
    path('saveuser/', views.saveuser, name="saveuser"),
    path('login/', views.auth_login, name="login"),
    path('auth/', views.auth, name="auth"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('savepost/', views.savepost, name="savepost"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.updatepost, name="updatepost"),
    path('logout/', views.auth_logout, name="logout"),
]