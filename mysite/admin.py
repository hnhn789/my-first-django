from django.contrib import admin

import account.admin
from .models import UserProfile, Story, ShoppingRecord, ItemList



class UserPointsAdmin(admin.ModelAdmin):

    list_display = ["user", "real_name", "usable_points", "history_points","opened_story"]


class StoryAdmin(admin.ModelAdmin):
    list_display = ["pk","topic", "content"]

class ShoppingAdmin(admin.ModelAdmin):
    list_display = ["buyer","item", "number"]


class ItemAdmin(admin.ModelAdmin):
    list_display = ["pk","name","price", "remain"]

admin.site.register(UserProfile, UserPointsAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(ShoppingRecord, ShoppingAdmin)
admin.site.register(ItemList, ItemAdmin)