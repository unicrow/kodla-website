# Third-Party
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


def set_speaker_image_upload_path(instance, filename):
    if instance.__class__.__name__ == 'Speaker':
        return '/'.join([
            'speakers', 'speaker_%d' % instance.id, 'images', filename
        ])
    else:
        return '/'.join([
            'speaker_requests', 'speaker_request_%d' % instance.id,
            'images', filename
        ])


class SpeakerModel(DateModel):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)
    image = models.ImageField(
        verbose_name=_('Image'), null=True, blank=True,
        upload_to=set_speaker_image_upload_path
    )
    company = models.CharField(
        verbose_name=_('Company'), max_length=255, null=True, blank=True
    )
    position = models.CharField(
        verbose_name=_('Position'), null=True, blank=True, max_length=255
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(SpeakerModel, self).save(*args, **kwargs)
            self.image = saved_image

        return super(SpeakerModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )

    def image_prev(self):
        if self.image:
            return '<img src="%s" style="max-height: 200px; ' \
                   'background-color:rgba(0, 0, 0, 0.1);"/>' % (
                        settings.MEDIA_URL + self.image.name
                    )
        else:
            return _('Not Found!')
    image_prev.short_description = _('Preview')
    image_prev.allow_tags = True


class SpeakerSocialAccountModel(DateModel):
    url = models.URLField(verbose_name=_('URL'))
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    account = models.ForeignKey(
        verbose_name=_('Account'), to='core.SocialAccount'
    )

    class Meta:
        abstract = True


class Speaker(SpeakerModel, SortableMixin):
    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')
        ordering = ('order_id', 'first_name', 'last_name')
        unique_together = ('first_name', 'last_name')

    def social_accounts(self):
        text = '<a href="{url}" target="_blank">{name}</a>'

        social_accounts = self.speakersocialaccount_set.all()
        social_accounts_text = [
            text.format(url=i.url, name=i.account.name) for i in social_accounts
        ]

        if social_accounts:
            return ', '.join(social_accounts_text)
        else:
            return '---'
    social_accounts.short_description = _('Social Accounts')
    social_accounts.allow_tags = True


class SpeakerSocialAccount(SpeakerSocialAccountModel, SortableMixin):
    speaker = models.ForeignKey(verbose_name=_('Speaker'), to='speaker.Speaker')

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Speaker Social Account')
        verbose_name_plural = _('Speaker Social Accounts')
        ordering = ('order_id', 'account')
        unique_together = ('speaker', 'account')

    def __str__(self):
        return '{speaker} - {account}'.format(
            speaker=self.speaker.__str__(), account=self.account.__str__()
        )


class SpeakerApplicationType(DateModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _('Speaker Application Type')
        verbose_name_plural = _('Speaker Application Types')
        ordering = ('name',)

    def __str__(self):
        return '{name}'.format(name=self.name)


class SpeakerApplication(SpeakerModel):
    website = models.URLField(verbose_name=_('Website'), null=True, blank=True)
    twitter = models.URLField(verbose_name=_('Twitter'), null=True, blank=True)
    github = models.URLField(verbose_name=_('Github'), null=True, blank=True)
    linkedin = models.URLField(verbose_name=_('Linkedin'), null=True, blank=True)
    other_social_account = models.URLField(
        verbose_name=_('Other Social Account'), null=True, blank=True
    )
    note = models.TextField(verbose_name=_('Note'), null=True, blank=True)
    application_type = models.ForeignKey(
        verbose_name=_('Application Type'), null=True, blank=True,
        to='speaker.SpeakerApplicationType'
    )
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    class Meta:
        verbose_name = _('Speaker Application')
        verbose_name_plural = _('Speaker Applications')
        ordering = ('activity', 'first_name', 'last_name')
        unique_together = (
            'activity', 'application_type', 'first_name', 'last_name'
        )
