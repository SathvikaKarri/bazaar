from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class item(models.Model):
    item_name = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.item_name
    
class cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.id

class CartItem(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE, related_name="procuctitem")
    cart = models.ForeignKey(cart, on_delete=models.CASCADE, related_name="cartitem")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.item.item_name