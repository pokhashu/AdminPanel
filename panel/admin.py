from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

admin.site.site_header = "Панель администрирования (Бот Погода)"
admin.site.site_title = "Администратор"
admin.site.index_title = "Добро пожаловать"

admin.site.unregister(User)
admin.site.unregister(Group)


class PublicatonAdmin(admin.ModelAdmin):
    list_display = ("city", "time")
    search_fields = ("city", "time")


class GroupsAdmin(admin.ModelAdmin):
    list_display = ("name", "chat_id", "city", "approved")
    list_editable = ("approved", "city")


admin.site.register(Publicaton, PublicatonAdmin)
admin.site.register(Groups, GroupsAdmin)
