# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel
from activity.models import Activity


class Contact(DateModel):
    full_name = models.CharField(verbose_name=_('Full Name'), max_length=100)
    email = models.EmailField(verbose_name=_('Email'))
    message = models.TextField(verbose_name=_('Message'))
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    activity = models.ForeignKey(verbose_name=_('Activity'), to=Activity)

    class Meta:
        verbose_name = _('Contant')
        verbose_name_plural = _('Contant')
        ordering = ('activity', '-create_date', '-update_date')

    def __str__(self):
        return '{full_name}'.format(full_name=self.full_name)
