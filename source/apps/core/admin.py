# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import SocialAccount


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'style_id', 'style_class')
    readonly_fields = ('create_date', 'update_date')
