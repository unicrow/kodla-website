# Django
from django.contrib import admin

# Local Django
from form.models import Contact, Register


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = (
        'activity', 'full_name', 'email',
        'message', 'is_active', 'create_date', 'update_date'
    )
    readonly_fields = ('create_date', 'update_date')

    list_display = (
        'activity', 'full_name', 'email', 'create_date', 'update_date', 'is_active'
    )
    list_filter = ('activity', 'is_active', 'create_date', 'update_date')
    list_editable = ('is_active',)
    search_fields = ('activity__name', 'full_name', 'email')


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    fields = (
        'activity', 'first_name', 'last_name', 'email', 'phone_number',
        'is_active', 'is_completed', 'create_date', 'update_date'
    )
    readonly_fields = ('create_date', 'update_date')

    list_display = (
        'activity', 'first_name', 'last_name', 'email', 'phone_number',
        'create_date', 'update_date', 'is_active', 'is_completed'
    )
    list_filter = (
        'activity', 'is_active', 'is_completed', 'create_date', 'update_date'
    )
    list_editable = ('is_active', 'is_completed')
    search_fields = ('activity__name', 'first_name', 'last_name', 'email')
