from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)



# Register your models here.
