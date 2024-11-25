from django.contrib import admin
from .models import Upload

class UploadedAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'uploaded_at']

admin.site.register(Upload, UploadedAdmin)


