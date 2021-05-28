from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    fields = ['username','password']

admin.site.register(Content, ContentAdmin)
