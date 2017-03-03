# Third-Party
from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableStackedInline

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from speaker.models import Speaker, SpeakerSocialAccount


class SpeakerSocialAccountInline(SortableStackedInline):
    model = SpeakerSocialAccount
    extra = 0
    verbose_name = _('Social Account')
    verbose_name_plural = _('Social Accounts')
    readonly_fields = ('create_date', 'update_date')
    fields = ('url', 'account', 'is_active', ('create_date', 'update_date'))


@admin.register(Speaker)
class SpeakerAdmin(SortableAdmin):
    fieldsets = (
        (_(u'Base'), {
            'fields' : ('first_name', 'last_name', ('image', 'image_prev')),
        }),
        (_(u'Detail'), {
            'fields' : ('is_active', ('create_date', 'update_date')),
        }),
    )

    readonly_fields = ('create_date', 'update_date', 'image_prev')
    list_display = (
        'first_name', 'last_name', 'social_accounts', 'is_active', 'image_prev'
    )
    list_filter = ('is_active', 'create_date', 'update_date')
    search_fields = ('first_name', 'last_name')
    inlines = (SpeakerSocialAccountInline,)
