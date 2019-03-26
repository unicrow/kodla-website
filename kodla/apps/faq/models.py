# Third-Party
from adminsortable.models import SortableMixin

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel

class Question(DateModel, SortableMixin):
    question = models.TextField(verbose_name=_('Question'))
    answer = models.TextField(verbose_name=_('Answer'))
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ('order_id', 'activity', 'question')