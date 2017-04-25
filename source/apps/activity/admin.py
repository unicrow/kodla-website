# Third-Party
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from activity.forms import ActivityAdminForm
from activity.models import (
    Activity, ActivityDocument,
    ActivitySocialAccount, ActivitySponsor, ActivityMap
)


class ActivityDocumentInline(admin.StackedInline):
    model = ActivityDocument
    extra = 0
    max_num = 1
    verbose_name = _('Document')
    verbose_name_plural = _('Documents')
    readonly_fields = ('create_date', 'update_date')
    fields = ('document', 'is_active', ('create_date', 'update_date'))


class ActivitySocialAccountInline(SortableStackedInline):
    model = ActivitySocialAccount
    extra = 0
    verbose_name = _('Social Account')
    verbose_name_plural = _('Social Accounts')
    readonly_fields = ('create_date', 'update_date')
    fields = (('account', 'url'), 'is_active', ('create_date', 'update_date'))


class ActivitySponsorInline(SortableStackedInline):
    model = ActivitySponsor
    extra = 0
    verbose_name = _('Sponsor')
    verbose_name_plural = _('Sponsors')
    readonly_fields = ('create_date', 'update_date')
    fields = (
        ('sponsor', 'sponsor_type'), ('logo_height', 'logo_width'),
        'is_active', ('create_date', 'update_date')
    )


class ActivityMapInline(admin.StackedInline):
    model = ActivityMap
    extra = 1
    max_num = 1
    verbose_name = _('Map')
    verbose_name_plural = _('Maps')
    readonly_fields = ('create_date', 'update_date')
    fields = (
        'description', 'is_active', ('create_date', 'update_date'), 'coordinates'
    )


@admin.register(Activity)
class ActivityAdmin(NonSortableParentAdmin):
    fieldsets = (
        (_(u'Base'), {
            'fields' : ('year', 'is_active'),
        }),
        (_(u'Feature'), {
            'fields' : (
                'has_speaker_application', 'has_register_url',
                'has_hackathon_register_url', 'has_activity_document'
            ),
        }),
        (_(u'Detail'), {
            'fields' : (
                'email', 'short_description', 'register_url',
                'hackathon_register_url', 'description', 'meta_tags',
                'logo', ('create_date', 'update_date')
            ),
        }),
        (_(u'Transportation'), {
            'fields' : ('address', 'transportation', 'accommodation'),
        }),
        (_(u'Speaker'), {
            'fields' : ('speakers',),
        })
    )

    form = ActivityAdminForm

    filter_horizontal = ('speakers',)
    readonly_fields = ('create_date', 'update_date')
    list_display = (
        'year', 'show_register_url', 'show_hackathon_register_url',
        'short_description', 'has_speaker_application', 'has_register_url',
        'has_hackathon_register_url', 'has_activity_document', 'is_active'
    )
    list_filter = ('is_active',)
    list_editable = (
        'has_speaker_application', 'has_register_url',
        'has_hackathon_register_url', 'has_activity_document', 'is_active'
    )
    search_fields = ('year',)
    inlines = (
        ActivityDocumentInline, ActivitySocialAccountInline,
        ActivitySponsorInline, ActivityMapInline
    )
