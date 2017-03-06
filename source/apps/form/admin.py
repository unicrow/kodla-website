# Django
from django.contrib import admin

# Local Django
from form.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = ('activity', 'full_name', 'email', 'is_active')
    list_filter = ('is_active', 'create_date', 'update_date', 'activity')
    search_fields = ('activity__name', 'full_name', 'email')
