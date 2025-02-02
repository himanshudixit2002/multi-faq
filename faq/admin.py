from django.contrib import admin
from .models import FAQ
from django.utils.html import format_html

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('truncated_question', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at', 'preview_answer')
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
        ('Metadata', {
            'fields': ('preview_answer', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def truncated_question(self, obj):
        return obj.question[:75] + '...' if len(obj.question) > 75 else obj.question
    truncated_question.short_description = 'Question'

    def preview_answer(self, obj):
        return format_html(f'<div style="max-height: 200px; overflow-y: auto;">{obj.answer}</div>')
    preview_answer.short_description = 'Formatted Answer'
