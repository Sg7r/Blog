from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    fields = ('data', 'content', 'image',)
    list_display = ('data', 'content', 'image','reaction_positive', 'reaction_negative',)
    list_editable = ('reaction_negative',)
    list_filter = ('data',)



admin.site.register(Content, ContentAdmin)