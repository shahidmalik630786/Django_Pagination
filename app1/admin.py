from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'disc', 'publish_date')