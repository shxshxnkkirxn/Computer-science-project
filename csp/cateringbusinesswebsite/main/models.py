from django.contrib.auth.models import User
from django.db import models
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @classmethod
    def create_user(cls, username, email, password):
        user = User.objects.create_user(username=username, email=email, password=password)
        return cls.objects.create(user=user)

class Item(models.Model):
    item_name = models.CharField(max_length=100, unique=False, default='')
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity=models.IntegerField(default=0)

class Menu(models.Model):
    items = models.ManyToManyField(Item, related_name='menus')
    menu_item = models.CharField(max_length=100, unique=False, default='')
    menu_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_models')
    menu = models.ManyToManyField(Menu, related_name='orders')
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

