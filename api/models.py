from django.db import models
from django.contrib.auth.models import AbstractUser


class Role (models.Model):
    role_name = models.CharField(unique=True, max_length=30)

class User (models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    sex = models.BooleanField(null=True)
    exp = models.IntegerField(default=0)

class Problem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    # update_date = models.DateField(default=date.today)
    content = models.TextField()
    exp = models.IntegerField()

class SolveStatus(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    last_code_path = models.TextField(default="")

class Topic(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    create_date = models.DateField(auto_now_add=True)

class Challenge(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()