from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=150, unique=True)
#     password = models.CharField(max_length=200)

#     def __str__(self):
#         return self.username


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

