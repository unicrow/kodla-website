# Third-Party
from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableStackedInline

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from speaker.models import (
    Speaker, SpeakerSocialAccount,
    SpeakerApplication, SpeakerApplicationSocialAccount
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
    search_fields = ('first_name', 'last_name')
    inlines = (SpeakerSocialAccountInline,)


class SpeakerApplicationSocialAccountInline(admin.StackedInline):
    model = SpeakerApplicationSocialAccount
    extra = 0
    verbose_name = _('Social Account')
    verbose_name_plural = _('Social Accounts')
    readonly_fields = ('create_date', 'update_date')
    fields = (('account', 'url'), 'is_active', ('create_date', 'update_date'))


@admin.register(SpeakerApplication)
class SpeakerApplicationAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'Base'), {
            'fields' : (
                'activity', 'first_name', 'last_name',
                'email', ('image', 'image_prev'),
            ),
        }),
        (_(u'Detail'), {
            'fields' : (
                'corporation', 'positions',
                'is_active', ('create_date', 'update_date')
            ),
        }),
    )

    readonly_fields = ('create_date', 'update_date', 'image_prev')
    list_display = (
        'activity', 'first_name', 'last_name',
        'social_accounts', 'image_prev', 'is_active'
    )
    list_filter = ('activity', 'is_active', 'create_date', 'update_date')
    list_editable = ('is_active',)
    search_fields = ('activity__name', 'first_name', 'last_name')
    inlines = (SpeakerApplicationSocialAccountInline,)
