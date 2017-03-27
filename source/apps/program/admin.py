# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from program.models import Program, ProgramContent


class ProgramContentInline(admin.StackedInline):
    model = ProgramContent
    extra = 0
    verbose_name = _('Program Content')
    verbose_name_plural = _('Program Contents')
    filter_horizontal = ('speakers',)
    readonly_fields = ('create_date', 'update_date')
    fields = (
        ('subject', 'annotation'), ('start_time', 'end_time'),
        ('program', 'speakers'), ('presentation_url', 'presentation_document'),
        'is_active', ('create_date', 'update_date')
    )


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = ('activity', 'date', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    inlines = (ProgramContentInline,)
