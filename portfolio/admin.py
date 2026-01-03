from django.contrib import admin
from django.utils.html import format_html
from .models import Book, PurchaseLink


# Это позволяет добавлять ссылки внутри страницы Книги
class PurchaseLinkInline(admin.TabularInline):
    model = PurchaseLink
    extra = 1  # Показывает одну пустую строку для новой ссылки по умолчанию

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_cover', 'is_visible')
    list_filter = ('is_visible',)
    search_fields = ('title', 'description')
    
    # Подключаем инлайн-редактирование ссылок
    inlines = [PurchaseLinkInline]

    def display_cover(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.cover_image.url)
        return "-"
    display_cover.short_description = "Cover"