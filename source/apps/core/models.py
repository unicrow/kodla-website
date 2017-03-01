# Third-Party
from adminsortable.models import SortableMixin

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DateModel(models.Model):
    create_date = models.DateTimeField(
        verbose_name=_('Create Date'), auto_now_add=True, editable=False
    )
    update_date = models.DateTimeField(
        verbose_name=_('Update Date'), auto_now=True, editable=False
    )

    class Meta:
        abstract = True


class SocialAccount(DateModel, SortableMixin):
    name = models.CharField(verbose_name=_('Name'), max_length=50, unique=True)
    style_id = models.CharField(
        verbose_name=_('Style Id'), max_length=100, null=True, blank=True,
    )
    style_class = models.CharField(
        verbose_name=_('Style Class'), max_length=100, null=True, blank=True
    )

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Social Account')
        verbose_name_plural = _('Social Accounts')
        ordering = ('order_id', 'name')

    def __str__(self):
        return '{name}'.format(name=self.name)
