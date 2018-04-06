# Third-Party
from import_export.admin import ExportMixin

# Django
from django.contrib import admin

# Local Django
from form.models import Contact, Register
from form.resources import RegisterResource


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = (
        'activity', 'full_name', 'email',
        'message', 'is_active', 'create_date', 'update_date'
    )
    readonly_fields = ('create_date', 'update_date')

    list_display = (
        'full_name', 'email', 'create_date', 'update_date', 'is_active', 'activity'
    )
    list_filter = ('activity', 'is_active', 'create_date', 'update_date')
    search_fields = ('full_name', 'email')


@admin.register(Register)
class RegisterAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RegisterResource

    fields = (
        'activity', 'first_name', 'last_name', 'email',
        'phone_number', 'tshirt_size', 'is_same_city', 'is_coming',
        'is_active', 'is_completed', 'create_date', 'update_date'
    )
    readonly_fields = ('create_date', 'update_date')

    list_display = (
        'first_name', 'last_name', 'email', 'tshirt_size', 'phone_number',
        'is_same_city', 'is_coming', 'is_active', 'is_completed', 'activity'
    )
    list_filter = (
        'activity', 'is_same_city', 'is_coming', 'is_active',
        'is_completed', 'tshirt_size', 'create_date', 'update_date'
    )
    search_fields = ('first_name', 'last_name', 'email')
    order_fields = ('activity',)
