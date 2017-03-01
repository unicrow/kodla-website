# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from activity.forms import ActivityAdminForm
from activity.models import (
    Activity, ActivitySocialAccount, ActivityMap, ActivityDocument
)


class ActivitySocialAccountInline(admin.StackedInline):
    model = ActivitySocialAccount
    fields = ('url', 'account', ('create_date', 'update_date'))
    readonly_fields = ('create_date', 'update_date')
    extra = 0
    verbose_name_plural = _('Activity Social Account')


class ActivityMapInline(admin.StackedInline):
    model = ActivityMap
    fields = ('description', ('create_date', 'update_date'), 'coordinates')
    readonly_fields = ('create_date', 'update_date')
    extra = 1
    max_num = 1
    verbose_name_plural = _('Activity Map')


class ActivityDocumentInline(admin.StackedInline):
    model = ActivityDocument
    fields = ('document', ('create_date', 'update_date'))
    readonly_fields = ('create_date', 'update_date')
    extra = 0
    max_num = 1
    verbose_name_plural = _('Activity Document')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'Base'), {
            'fields' : (
                'year', 'short_description', 'register_url',
                'description', 'meta_tags', 'logo', 'is_active',
                ('create_date', 'update_date')
            ),
        }),
        (_(u'Speaker'), {
            'fields' : ('speakers',),
        }),
        (_(u'Transportation'), {
            'fields' : ('address', 'transportation', 'accommodation'),
        })
    )

    form = ActivityAdminForm

    filter_horizontal = ('speakers',)
    list_display = ('year', 'show_register_url', 'short_description', 'is_active')
    readonly_fields = ('create_date', 'update_date')
    inlines = (
        ActivitySocialAccountInline, ActivityDocumentInline, ActivityMapInline
    )
