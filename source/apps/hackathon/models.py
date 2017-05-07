# Third-Party
from adminsortable.models import SortableMixin

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


def set_activity_hackathon_upload_path(instance, filename):
    return '/'.join([
        'activities', 'activity_%d' % instance.activity.id,
        'hackathon', 'default', filename
    ])

class Hackathon(DateModel):
    register_url = models.URLField(
        verbose_name=_('Register URL'), null=True, blank=True
    )
    has_register_url = models.BooleanField(
        verbose_name=_('Register URL'), default=True
    )
    description = models.TextField(
        verbose_name=_('Description'), null=True, blank=True
    )
    has_description = models.BooleanField(
        verbose_name=_('Description'), default=False
    )
    team_description = models.TextField(
        verbose_name=_('Team Description'), null=True, blank=True
    )
    has_team_description = models.BooleanField(
        verbose_name=_('Team Description'), default=False
    )
    has_comment = models.BooleanField(verbose_name=_('Comment'), default=False)
    has_prize = models.BooleanField(verbose_name=_('Prize'), default=False)
    main_image = models.ImageField(
        verbose_name=_('Main Image'), null=True, blank=True,
        upload_to=set_activity_hackathon_upload_path
    )
    main_image_height = models.PositiveSmallIntegerField(
        verbose_name=_('Main Image Height'), null=True, blank=True
    )
    main_image_width = models.PositiveSmallIntegerField(
        verbose_name=_('Main Image Width'), null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'))
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    class Meta:
        verbose_name = _('Hackathon')
        verbose_name_plural = _('Hackathons')
        ordering = ('activity',)

    def __str__(self):
        return '{year} Hackathon'.format(year=self.activity.year)

    def show_register_url(self):
        if self.register_url:
            return "<a href='%s' target='_blank'>%s</a>" % (
                self.register_url, self.register_url
            )

        return self.register_url
    show_register_url.allow_tags = True
    show_register_url.short_description = _('Register URL')

    def main_image_prev(self):
        if self.main_image:
            return '<img src="%s" style="max-height: 100px; ' \
                   'background-color:rgba(0, 0, 0, 0.1);"/>' % (
                        settings.MEDIA_URL + self.main_image.name
                   )
        else:
            return _('Not Found!')
    main_image_prev.short_description = _('Preview')
    main_image_prev.allow_tags = True


def set_activity_hackathon_prize_upload_path(instance, filename):
    return '/'.join([
        'activities', 'activity_%d' % instance.hackathon.activity.id,
        'hackathon', 'prizes', 'prize_%d' % instance.id, filename
    ])


class HackathonPrize(DateModel, SortableMixin):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(
        verbose_name=_('Description'), null=True, blank=True
    )
    main_image = models.ImageField(
        verbose_name=_('Main Image'), null=True, blank=True,
        upload_to=set_activity_hackathon_prize_upload_path
    )
    main_image_height = models.PositiveSmallIntegerField(
        verbose_name=_('Main Image Height'), null=True, blank=True
    )
    main_image_width = models.PositiveSmallIntegerField(
        verbose_name=_('Main Image Width'), null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'))
    hackathon = models.ForeignKey(
        verbose_name=_('Hackathon'), to='hackathon.Hackathon'
    )

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Hackathon Prize')
        verbose_name_plural = _('Hackathon Prizes')
        ordering = ('order_id',)

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_main_image = self.main_image
            self.main_image = None
            super(HackathonPrize, self).save(*args, **kwargs)
            self.main_image = saved_main_image

        return super(HackathonPrize, self).save(*args, **kwargs)

    def __str__(self):
        return '{name}'.format(name=self.name)

    def main_image_prev(self):
        if self.main_image:
            return '<img src="%s" style="max-height: 100px; ' \
                   'background-color:rgba(0, 0, 0, 0.1);"/>' % (
                        settings.MEDIA_URL + self.main_image.name
                   )
        else:
            return _('Not Found!')
    main_image_prev.short_description = _('Preview')
    main_image_prev.allow_tags = True
