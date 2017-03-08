# Third-Party
from adminsortable.models import SortableMixin

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


class SponsorType(DateModel, SortableMixin):
    name = models.CharField(verbose_name=_('Name'), max_length=100, unique=True)
    description = models.TextField(
        verbose_name=_('Description'), null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Sponsor Type')
        verbose_name_plural = _('Sponsor Types')
        ordering = ('order_id', 'name')

    def __str__(self):
        return '{name}'.format(name=self.name)


def set_sponsor_logo_upload_path(instance, filename):
    return '/'.join(['sponsors', 'sponsor_%d' % instance.id, 'logo', filename])


class Sponsor(DateModel):
    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    logo = models.ImageField(
        verbose_name=_('Logo'), null=True, blank=True,
        upload_to=set_sponsor_logo_upload_path
    )
    logo_width = models.PositiveSmallIntegerField(
        verbose_name=_('Logo Width'), null=True, blank=True
    )
    logo_height = models.PositiveSmallIntegerField(
        verbose_name=_('Logo Height'), null=True, blank=True
    )

    class Meta:
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')
        ordering = ('name',)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_logo = self.logo
            self.logo = None
            super(Sponsor, self).save(*args, **kwargs)
            self.logo = saved_logo

        return super(Sponsor, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}'.format(name=self.name)

    def logo_prev(self):
        if self.logo:
            return '<img src="%s" style="max-height: 200px; ' \
                   'background-color:rgba(0, 0, 0, 0.1);"/>' % (
                        settings.MEDIA_URL + self.logo.name
                   )
        else:
            return _('Not Found!')
    logo_prev.short_description = _('Preview')
    logo_prev.allow_tags = True
