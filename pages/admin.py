from django.contrib import admin
from .models import Content

from django.contrib.auth.models import Group
admin.site.unregister(Group)

admin.site.site_header = 'My Sandbox Django Admin Page'
admin.site.site_title  =  "Custom Site Title"
admin.site.index_title  =  "Custom index Admin"

class ContentAdmin(admin.ModelAdmin):
    fields = ['username', 'password']

    list_display = ("username", "password")

admin.site.register(Content, ContentAdmin)
