# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from activity.models import Activity, ActivityMap, ActivityDocument


class ActivityMapInline(admin.StackedInline):
    model = ActivityMap
    extra = 1
    max_num = 1
    verbose_name_plural = _('Activity Map')


class ActivityDocumentInline(admin.StackedInline):
    model = ActivityDocument
    extra = 0
    max_num = 1
    verbose_name_plural = _('Activity Document')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = (ActivityDocumentInline, ActivityMapInline,)

    list_display = ('year', 'show_register_url', 'short_description')
