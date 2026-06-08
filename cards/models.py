from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.forms import forms

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return f'{self.name} | {self.email} | {self.username} | IS_SUPERUSER: {self.is_superuser}'


class CustomUserManager:
    def create_superuser(self, email, name, username, password, **kwargs):
        user = User.objects.create_user(
            email=email,
            name=name,
            username=username,
            password=password,
            is_superuser=True,
            **kwargs
        )
        return user


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.tag


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# i.e. this is the database tables model
# Create your models here.
class Card(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=700)
    tag = models.ManyToManyField(Tag)
    box = models.IntegerField(choices=zip(BOXES, BOXES),
                              default=BOXES[0])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.question}'

    def move(self, solved):
        move_to_box = self.box + 1 if solved else BOXES[0]
        if move_to_box in BOXES:
            self.box = move_to_box
            self.save()
        return self
