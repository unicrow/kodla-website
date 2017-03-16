# Django
from django.contrib import admin

# Local Django
from form.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = (
        'activity', 'full_name', 'email', 'create_date', 'update_date', 'is_active'
    )
    list_filter = ('activity', 'is_active', 'create_date', 'update_date')
    list_editable = ('is_active',)
    search_fields = ('activity__name', 'full_name', 'email')
