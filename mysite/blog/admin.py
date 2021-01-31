from django.contrib import admin
from . models import Post  # added Post model to regiter in Django admin site 

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)  # Decorator to register
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')