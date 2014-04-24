#!python
#encoding:utf-8
from django.contrib import admin
from api.models import *


class TagAdmin(admin.ModelAdmin):
    list_display = (  'id', 'mall','name', 'type', 'description', 'create_date', 'modified_date')
    list_display_links = ('name',)
    list_filter = ( 'type', 'mall',)
    #ordering = ( 'create_date',)
    search_fields = ( 'name',)


admin.site.register(Tag, TagAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'mall','title', 'type', 'description', 'start_time', 'end_time', 'create_date',
        'modified_date',)  #'image', 'url',
    list_display_links = ('title',)
    list_filter = ( 'type', 'mall',)
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Subject, SubjectAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'mall','name', 'gender', 'deviceId', 'app_secret', 'mobile', 'club_card', 'create_date', 'modified_date',)
    list_display_links = ('name',)
    list_filter = ( 'gender','mall', )
    #ordering = ( 'create_date',)
    search_fields = ( 'name', 'deviceId', 'mobile', )


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
        'id', 'mall','title', 'follower_count', 'comment_count', 'logo', 'tel', 'homepage', 'create_date', 'modified_date',)
    list_display_links = ('title',)
    list_filter = ( 'mall',)
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Store, StoreAdmin)


class GoodsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'mall','title', 'store', 'brand_name', 'cover_img', 'create_date', 'modified_date',)
    list_display_links = ('title',)
    list_filter = ( 'mall', )
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Goods, GoodsAdmin)


class PromotionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'mall','title', 'type', 'collect_count', 'comment_count', 'store', 'is_bank_special', 'create_date',
        'modified_date',)
    list_display_links = ('title',)
    list_filter = ( 'type', 'mall',)
    #ordering = ( 'create_date',)
    search_fields = ( 'title',)


admin.site.register(Promotion, PromotionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'mall','name', 'create_date', 'modified_date',)
    list_display_links = ('name',)
    list_filter = ( 'mall',)
    #ordering = ( 'create_date',)
    search_fields = ( 'name',)


admin.site.register(Category, CategoryAdmin)


class MallAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'mall_code', 'app_name', 'create_date', 'modified_date',)
    list_display_links = ('name',)
    #list_filter = ( 'type', )
    #ordering = ( 'create_date',)
    search_fields = ( 'name',)


admin.site.register(Mall, MallAdmin)

class SearchKeywordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'keyword', 'mall', 'create_date', 'modified_date',)
    list_display_links = ('keyword',)
    list_filter = ( 'mall', )
    #ordering = ( 'create_date',)
    search_fields = ( 'keyword',)


admin.site.register(SearchKeyword, SearchKeywordAdmin)

