from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsersManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        # Buat user baru dengan menggunakan phone_number sebagai identitas unik
        if not phone_number:
            raise ValueError('The phone number field must be set')
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        # Buat superuser dengan menggunakan phone_number sebagai identitas unik
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)


class UserBsl(AbstractUser):
    LEVEL_CHOICES = [
        ('0', 'VISIT'),
        ('1', 'STAFF'),
        ('2', 'LEAD'),
        ('3', 'ADMIN'),
    ]
    phone_number = models.CharField(null=False, blank=False, unique=True, max_length=14)
    uid = models.CharField(null=False, blank=False, unique=True, max_length=120)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    level = models.CharField(max_length=40, choices=LEVEL_CHOICES, default='0')

    USERNAME_FIELD = 'phone_number'
    objects = UsersManager()

    def __str__(self):
        return self.phone_number
    

class Notification(models.Model):
    title = models.CharField(max_length=30, null=False)
    content = models.CharField(max_length=100, null=False)
    # to = models.ForeignKey(Department, on_delete=models.CASCADE)