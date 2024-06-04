from django.contrib import admin
from .models import Send

@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ['phone', 'city', 'turn', 'created']

