# Third-Party
from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableStackedInline

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from speaker.models import (
    Speaker, SpeakerSocialAccount, SpeakerApplicationType, SpeakerApplication
)


class SpeakerSocialAccountInline(SortableStackedInline):
    model = SpeakerSocialAccount
    extra = 0
    verbose_name = _('Social Account')
    verbose_name_plural = _('Social Accounts')
    readonly_fields = ('create_date', 'update_date')
    fields = (('account', 'url'), 'is_active', ('create_date', 'update_date'))


@admin.register(Speaker)
class SpeakerAdmin(SortableAdmin):
    fieldsets = (
        (_(u'Base'), {
            'fields' : (
                'first_name', 'last_name', 'email', ('image', 'image_prev')
            ),
        }),
        (_(u'Company'), {
            'fields' : ((('company', 'company_url'), 'position')),
        }),
        (_(u'Detail'), {
            'fields' : ('is_active', ('create_date', 'update_date')),
        }),
    )

    readonly_fields = ('create_date', 'update_date', 'image_prev')
    list_display = (
        'first_name', 'last_name', 'social_accounts', 'image_prev', 'is_active'
    )
    list_filter = ('is_active', 'create_date', 'update_date')
    list_editable = ('is_active',)
    search_fields = ('first_name', 'last_name', 'company', 'position')
    inlines = (SpeakerSocialAccountInline,)


@admin.register(SpeakerApplicationType)
class SpeakerApplicationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('name',)


@admin.register(SpeakerApplication)
class SpeakerApplicationAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'Base'), {
            'fields' : (
                'activity', 'application_type', 'email',
                'first_name', 'last_name', 'note', ('image', 'image_prev'),
            ),
        }),
        (_(u'Company'), {
            'fields' : ((('company', 'company_url'), 'position')),
        }),
        (_(u'Social Account'), {
            'fields' : ((
                'website', 'twitter', 'github', 'linkedin', 'other_social_account'
            )),
        }),
        (_(u'Detail'), {
            'fields' : (
                'is_active', ('create_date', 'update_date')
            ),
        })
    )

    readonly_fields = ('create_date', 'update_date', 'image_prev')
    list_display = (
        'activity', 'application_type', 'email',
        'first_name', 'last_name', 'image_prev', 'is_active'
    )
    list_filter = (
        'activity', 'application_type', 'is_active', 'create_date', 'update_date'
    )
    list_editable = ('is_active',)
    search_fields = (
        'activity__name', 'first_name', 'last_name', 'company', 'position'
    )
