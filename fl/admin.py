from django.contrib import admin
from .models import FlUpload

# Register your models here.
@admin.register(FlUpload)
class FileDisp(admin.ModelAdmin):
    list_display=['id', 'name']
