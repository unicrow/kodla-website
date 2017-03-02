# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from program.models import Program, ProgramContent


class ProgramContentInline(admin.StackedInline):
    model = ProgramContent
    fields = (
        ('subject', 'annotation'), ('start_time', 'end_time'),
        ('program', 'speaker'), 'is_active', ('create_date', 'update_date')
    )
    readonly_fields = ('create_date', 'update_date')
    extra = 0
    verbose_name_plural = _('Program Content')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('activity', 'date', 'is_active')
    readonly_fields = ('create_date', 'update_date')
    inlines = (ProgramContentInline,)
