#!python
#encoding:utf-8
from django.contrib import admin
from api.models import *


class TagAdmin(admin.ModelAdmin):
    list_display = (  'id', 'name', 'type', 'description', 'create_date', 'modified_date')
    list_display_links = ('name',)
    list_filter = ( 'type', )
    #ordering = ( 'create_date',)
    search_fields = ( 'name',)


admin.site.register(Tag, TagAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'type', 'description', 'start_time', 'end_time', 'create_date',
        'modified_date',)  #'image', 'url',
    list_display_links = ('title',)
    list_filter = ( 'type', )
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Subject, SubjectAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'gender', 'deviceId', 'app_secret', 'mobile', 'club_card', 'create_date', 'modified_date',)
    list_display_links = ('name',)
    list_filter = ( 'gender', )
    #ordering = ( 'create_date',)
    search_fields = ( 'name', 'deviceId','mobile', )


admin.site.register(User, UserAdmin)


class BankAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'create_date', 'modified_date',)
    list_display_links = ('name',)
    #list_filter = ( 'type','gender', )
    #ordering = ( 'create_date',)
    search_fields = ( 'name',)


admin.site.register(Bank, BankAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'follower_count', 'comment_count', 'logo', 'tel', 'homepage', 'create_date', 'modified_date',)
    list_display_links = ('title',)
    #list_filter = ( 'type', )
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Store, StoreAdmin)


class GoodsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'store', 'brand_name', 'cover_img', 'create_date', 'modified_date',)
    list_display_links = ('title',)
    # list_filter = ( 'type', )
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Goods, GoodsAdmin)

class PromotionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'type', 'collect_count', 'comment_count', 'store', 'is_bank_special', 'create_date', 'modified_date',)
    list_display_links = ('title',)
    list_filter = ( 'type', )
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Promotion, PromotionAdmin)