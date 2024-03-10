from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,name,phone_no,**extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")
        
        user = self.model(
            email= self.normalize_email(email),
            name=name,
            phone_no=phone_no,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,email,password,name,phone_no,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,name,phone_no,**extra_fields)
    
    def create_superuser(self,email,password,name,phone_no,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_active",True)
        extra_fields.setdefault("is_superuser",True)
        return self._create_user(email,password,name,phone_no,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(db_index=True,unique=True,max_length=254)
    name = models.CharField(max_length=128)
    phone_no = models.PositiveIntegerField(help_text='Contact phone number')

    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","phone_no"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email