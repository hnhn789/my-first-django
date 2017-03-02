from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    real_name = models.CharField(max_length=100,default="未命名")
    usable_points = models.IntegerField(default=0)
#    history_points = models.IntegerField(default=0)
#    opened_story = models.CharField(max_length=100, default="")
    bought_items = models.ForeignKey(BoughtItems, on_delete=models.CASCADE)
    QR_code_record = models.ForeignKey(QRCodeRecord)
'''
class Story(models.Model):
    number = models.IntegerField(default=0)
    story_name = models.CharField(max_length=100, default="未命名的故事")
    code = models.IntegerField(default=0)
'''

class ItemList(models.Model):
    name = models.CharField(max_length=100,blank=True)
    price = models.IntegerField(default=0)
    remain = models.IntegerField(default=0)

'''
class ShoppingRecord(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    #number = models.IntegerField(default=0)
'''

class BoughtItems(models.Model):
    item_name = models.IntegerField(default=0)
    item_quantity = models.IntegerField(default=0)
    bought_time = models.DateTimeField(auto_now_add=True, editable=False)

class QRCodeRecord(models.Model):
    code_content = models.CharField(max_length=200, default="")
    time = models.DateTimeField(auto_now_add=True, editable=False)