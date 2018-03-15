# Django
from django.contrib import admin

# Local Django
from form.models import Contact, Register


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = (
        'activity', 'full_name', 'email', 'create_date', 'update_date', 'is_active'
    )
    list_filter = ('activity', 'is_active', 'create_date', 'update_date')
    list_editable = ('is_active',)
    search_fields = ('activity__name', 'full_name', 'email')


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = (
        'activity', 'first_name', 'last_name', 'email',
        'create_date', 'update_date', 'is_active'
    )
    list_filter = ('activity', 'is_active', 'create_date', 'update_date')
    list_editable = ('is_active',)
    search_fields = ('activity__name', 'first_name', 'last_name', 'email')
