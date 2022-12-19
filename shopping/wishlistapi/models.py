from django.db import models

# Create your models here.
from oscar.core.loading import get_model

from django.contrib.auth import get_user_model
Product = get_model("catalogue", "Product")
User = get_user_model()

class WishListItems(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    #wishlist = models.ForeignKey(WishList,on_delete=models.CASCADE, related_name='wishlistitems')
    item = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)