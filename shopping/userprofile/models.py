from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.contrib.auth import get_user_model
# class User(AbstractUser):
#     username = models.CharField(blank=True, null=True, max_length=10)
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     def __str__(self):
#         return "{}".format(self.email)

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.title), filename])
User = get_user_model()
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    photo = models.FileField(upload_to=nameFile, blank=True)
    photo2 = models.FileField(upload_to=nameFile,blank=True)
    phone_number = models.CharField(max_length=8)
    updated_at = models.DateTimeField(auto_now_add=True)
    _metadata = {
        'title': 'title',
        'image': 'get_meta_image',
    }

    def get_meta_image(self):
        if self.photo:
            return self.photo.url


    def __str__(self) -> str:
        return self.title 