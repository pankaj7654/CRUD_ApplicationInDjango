from django.contrib import admin
from crud.models.user import User
from crud.models.product import Product
from django.utils.html import format_html


class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','password','active']
    sortable_by = ['id' , 'name']
    list_editable = ['active']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','quantity','price']
    sortable_by = ['name']

admin.site.register(User , UserAdmin)
admin.site.register(Product , ProductAdmin)
