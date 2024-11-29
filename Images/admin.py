from django.contrib import admin
from .models import Images

class ImagesAdmin(admin.ModelAdmin):
    fields = ('name', 'url')
    # list_display = ('name', 'url',)



admin.site.register(Images, ImagesAdmin)