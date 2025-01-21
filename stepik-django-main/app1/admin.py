from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')  # 'is_active' modelda mavjudligini tekshiring
    search_fields = ('name',)
    list_filter = ('is_active',)  # 'is_active' Field bo‘lishi kerak
