from django.contrib import admin
from .models import Post, Tag, Author
# Register your models here.

class PostAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "date",)
    list_display = ("title", "author", "date",)


class AuthorAdmin (admin.ModelAdmin):
    list_display = ("full_name", "email",)
    list_filter = ("last_name","email",)
    

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)