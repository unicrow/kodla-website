# Third-Party
from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableStackedInline

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from .models import Question

@admin.register(Question)
class QuestionAdmin(SortableAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = ('activity', 'question')