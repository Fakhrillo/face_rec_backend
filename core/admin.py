from django.contrib import admin
from .models import UserInfo, Photos_to_check


# Register your models here.
@admin.register(UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'fullname', 'photo')
    list_filter = ('fullname',)
    search_fields = ('fullname',)


@admin.register(Photos_to_check)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'photo')
    list_filter = ('user_id',)
    search_fields = ('user_id',)
