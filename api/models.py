from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from rest_framework.authtoken.views import Token

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('User must have email'))
        email = self.normalize_email(email)
        user  = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        # Token.objects.create(user=user)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class User (AbstractUser):
    username = None
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email     = models.EmailField(max_length=255, unique=True)
    exp       = models.IntegerField(default=0)
    sex       = models.BooleanField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Problem(models.Model):
    LEVEL = (
    ("BEGGINER","Beginner"),
    ("MIDDLE","Middle"),
    ("ADVANCE","Advance"),
)
    id        = models.IntegerField(primary_key=True)
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    description   = models.TextField()
    exp       = models.IntegerField()
    solve     = models.BooleanField(default=False)
    result    = models.CharField(max_length=50)
    level     = models.CharField(max_length=20, choices=LEVEL)

class SolveStatus(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    problem   = models.ForeignKey(Problem, on_delete=models.CASCADE)
    last_code_path = models.TextField(default="")
    isSolved  = models.BooleanField(default=False)

class Topic(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    title     = models.TextField()
    content   = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    isVerified  = models.BooleanField(default=False)

class Challenge(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    name      = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    end_date  = models.DateField()

class Class(models.Model):
    title     = models.CharField(max_length=50)
    content   = models.TextField()
    create_date = models.DateField(auto_now_add=True)

class Enrolment(models.Model):
    user_id      = models.ForeignKey(User, on_delete=models.CASCADE)
    class_id     = models.ForeignKey(Class, on_delete=models.CASCADE)
