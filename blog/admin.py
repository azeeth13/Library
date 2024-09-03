from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmins(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# admin.site.register(Category)
# admin.site.register(Book)

@admin.register(Category)
class KitobInfo(ArticleAdmins):
    list_display = ('name', 'id',)

@admin.register(Book)
class KitobInfo(ArticleAdmins):
    list_display = ('name', 'category', 'author', 'id',)


    
@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'book_id', 'created', 'id', 'comment',)