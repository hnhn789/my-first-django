from django.contrib import admin

import account.admin
from .models import UserProfile, ItemList, QRcodeList ,BoughtItems, QRCodeRecord, QRcodeStatus, BoughtRecord



class UserPointsAdmin(admin.ModelAdmin):
    list_display = ["pk", "username", "real_name", "usable_points"]

'''
class StoryAdmin(admin.ModelAdmin):
    list_display = ["pk","title", "content"]

class ShoppingAdmin(admin.ModelAdmin):
    list_display = ["buyer","item"]
'''

class ItemAdmin(admin.ModelAdmin):
    list_display = ["pk","name","price", "remain"]

class QRCodeAdmin(admin.ModelAdmin):
    list_display = ["pk", "code_content"]

class BoughtItemsAdmin(admin.ModelAdmin):
    list_display = ["pk", "item_name", "item_quantity", "user"]

class BoughtRecordAdmin(admin.ModelAdmin):
    list_display = ["user", "item_name", "bought_time"]

class QRCodeRecordAdmin(admin.ModelAdmin):
    list_display = ["code_content", "time",  "points_got", "user"]

class CodeStatusAdmin(admin.ModelAdmin):
    list_display = ["code", "last_read", "user"]



admin.site.register(UserProfile, UserPointsAdmin)
# admin.site.register(Story, StoryAdmin)
#admin.site.register(ItemList, ShoppingAdmin)
admin.site.register(ItemList, ItemAdmin)
admin.site.register(QRcodeList, QRCodeAdmin)
admin.site.register(BoughtItems, BoughtItemsAdmin)
admin.site.register(BoughtRecord, BoughtRecordAdmin)
admin.site.register(QRCodeRecord, QRCodeRecordAdmin)
admin.site.register(QRcodeStatus, CodeStatusAdmin)
