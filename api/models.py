from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


# class Role (models.Model):
#     role_name = models.CharField(unique=True, max_length=30)

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('User must have email'))
        email = self.normalize_email(email)
        user  = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
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

'''
    def create_user(self, email, password = None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user
'''
class User (AbstractUser):
    # role      = models.ForeignKey(Role, on_delete=models.CASCADE)
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
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    # update_date = models.DateField(default=date.today)
    content   = models.TextField()
    exp       = models.IntegerField()
    result    = models.CharField(max_length=50)

class SolveStatus(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    problem   = models.ForeignKey(Problem, on_delete=models.CASCADE)
    last_code_path = models.TextField(default="")

class Topic(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    title     = models.TextField()
    content   = models.TextField()
    create_date = models.DateField(auto_now_add=True)

class Challenge(models.Model):
    user      = models.ForeignKey(User,on_delete=models.CASCADE)
    name      = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    end_date  = models.DateField()
