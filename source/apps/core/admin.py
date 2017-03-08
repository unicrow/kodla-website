# Third-Party
from adminsortable.admin import SortableAdmin

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import SocialAccount


@admin.register(SocialAccount)
class SocialAccountAdmin(SortableAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = ('name', 'style_id', 'style_class', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('name',)
