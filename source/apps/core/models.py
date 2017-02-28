# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DateModel(models.Model):
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True, editable=False)
    update_date = models.DateTimeField(verbose_name=_('Update Date'), auto_now=True, editable=False)

    class Meta:
        abstract = True
