# Third-Party
from adminsortable.admin import NonSortableParentAdmin, SortableStackedInline

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from hackathon.models import Hackathon, HackathonPrize
from hackathon.forms import HackathonAdminForm, HackathonPrizeAdminForm


class HackathonPrizeInline(SortableStackedInline):
    model = HackathonPrize
    extra = 0
    verbose_name = _('Hackathon Prize')
    verbose_name_plural = _('Hackathon Prizes')
    readonly_fields = ('create_date', 'update_date', 'main_image_prev')
    fields = (
        'name', ('main_image', 'main_image_prev'),
        ('main_image_height', 'main_image_width'), 'description',
        'is_active', ('create_date', 'update_date')
    )
    form = HackathonPrizeAdminForm


@admin.register(Hackathon)
class HackathonAdmin(NonSortableParentAdmin):
    fieldsets = (
        (_(u'Base'), {
            'fields' : ('activity', 'is_active'),
        }),
        (_(u'Content'), {
            'fields' : (
                'register_url', 'has_register_url', 'has_comment',
                ('main_image', 'main_image_prev'),
                ('main_image_height', 'main_image_width'),
                'description', 'team_description'

            ),
        }),
        (_(u'Detail'), {
            'fields' : (
                'create_date', 'update_date'
            ),
        })
    )

    form = HackathonAdminForm

    list_display = (
        'activity', 'show_register_url', 'has_comment', 'has_register_url', 'is_active'
    )
    list_filter = ('has_comment', 'has_register_url', 'is_active')
    list_editable = ('has_comment', 'has_register_url', 'is_active')
    readonly_fields = ('create_date', 'update_date', 'main_image_prev')
    inlines = (HackathonPrizeInline,)
