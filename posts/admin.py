from django.contrib import admin
from .models import Post, Category


# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_filter = ['publishing_time']
    list_display = ['title', 'publishing_time']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


admin.site.register(Post, AdminPost)
admin.site.register(Category)
