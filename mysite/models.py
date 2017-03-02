from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    real_name = models.CharField(max_length=100,default="未命名")
    usable_points = models.IntegerField(default=0)
    history_points = models.IntegerField(default=0)
    opened_story = models.CharField(max_length=100, default="")
    bought_items = models.CharField(max_length=100, default="")



class Story(models.Model):
    points = models.IntegerField(default=0)
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField(blank=True)

class ItemList(models.Model):
    name = models.CharField(max_length=100,blank=True)
    price = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)

class ShoppingRecord(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    number = models.IntegerField(default=0);



