# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.variables import TSHIRT_SIZES
from core.models import DateModel, PhoneModel


class Contact(DateModel):
    full_name = models.CharField(verbose_name=_('Full Name'), max_length=100)
    email = models.EmailField(verbose_name=_('Email'))
    message = models.TextField(verbose_name=_('Message'))
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contact')
        ordering = ('activity', '-create_date', '-update_date')

    def __str__(self):
        return '{full_name}'.format(full_name=self.full_name)


class Register(DateModel, PhoneModel):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=100)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=100)
    email = models.EmailField(verbose_name=_('Email'))
    tshirt_size = models.PositiveSmallIntegerField(
        verbose_name=_('T-shirt Size'), choices=TSHIRT_SIZES, null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=False)
    is_completed = models.BooleanField(verbose_name=_('Completed'), default=False)
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    class Meta:
        verbose_name = _('Register')
        verbose_name_plural = _('Register')
        ordering = ('activity', '-create_date', '-update_date')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )
