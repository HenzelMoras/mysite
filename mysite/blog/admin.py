from django.contrib import admin
from . models import Post  # added Post model to regiter in Django admin site 

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)  # Decorator to register
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # list_display for displaying POst columns as Tuple index format
    list_filter = ('status', 'created', 'publish', 'author')  # Filter appears at the rightside of Post page 
    search_fields = ('title', 'body')             # search field
    prepopulated_fields = {'slug': ('title',)}   # Naming option based on slug will appear while creating a post               
    raw_id_fields = ('author',)     # id field for search bar using author foriegn key
    date_hierarchy = 'publish'     
    ordering = ('status', 'publish')
