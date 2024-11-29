from django.contrib import admin

from .models import Comments

class CommentsAdmin(admin.ModelAdmin):
    # fields = ('data', 'content_body', 'user', 'blog')
    # list_display = ('data', 'content_body', 'user', 'blog')

admin.site.register(Comments, CommentsAdmin)