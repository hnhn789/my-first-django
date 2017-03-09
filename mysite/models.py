from django.conf import settings
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from datetime import datetime

class UserProfile(models.Model):
    username = models.CharField(max_length=20, default="未命名", unique=True)
    real_name = models.CharField(max_length=100,default="未命名")
    usable_points = models.IntegerField(default=0)
#    history_points = models.IntegerField(default=0)
#    opened_story = models.CharField(max_length=100, default="")
#    bought_items = models.ForeignKey(BoughtItems, on_delete=models.CASCADE)
#    QR_code_record = models.ForeignKey(QRCodeRecord, on_delete=models.CASCADE)
 #   QR_code_status = models.ForeignKey(QRcodeStatus, on_delete=models.CASCADE)
    def __str__(self):
        return self.real_name
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

    def __str__(self):
        return self.name

'''
class ShoppingRecord(models.Model):
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemList, on_delete=models.CASCADE)
    #number = models.IntegerField(default=0)
'''

class BoughtItems(models.Model):
    item_name = models.IntegerField(default=0)
    item_quantity = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile)

class QRCodeRecord(models.Model):
    code_content = models.CharField(max_length=40, unique=False)
    time = models.DateTimeField(auto_now_add=True, editable=False)
    points_got = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile)

class QRcodeStatus(models.Model):
    code = models.SlugField(max_length=40, unique=True)
    last_read = models.DateTimeField(default=datetime.now(), editable=True)
    user = models.ForeignKey(UserProfile)

class QRcodeList(models.Model):
    code_content = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.code_content

class BoughtRecord(models.Model):
    user = models.ForeignKey(UserProfile)
    item_name = models.IntegerField(default=0)
    bought_time = models.DateTimeField(auto_now_add=True, editable=False)