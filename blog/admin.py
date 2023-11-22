from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text')
    raw_id_fields = ('post', 'author',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes',)


admin.site.register(Tag)
