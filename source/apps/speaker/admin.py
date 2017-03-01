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
    fields = ('url', 'account', ('create_date', 'update_date'))
    readonly_fields = ('create_date', 'update_date')
    extra = 0
    verbose_name_plural = _('Speaker Social Account')


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

    list_display = ('first_name', 'last_name', 'social_accounts', 'image_prev')
    readonly_fields = ('create_date', 'update_date', 'image_prev')
    inlines = (SpeakerSocialAccountInline,)
