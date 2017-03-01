# Third-Party
from adminsortable.models import SortableMixin

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel, SocialAccount


def set_speaker_image_upload_path(instance, filename):
    return '/'.join(['speakers', 'speaker_%d' % instance.id, filename])


class Speaker(DateModel, SortableMixin):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    image = models.ImageField(
        verbose_name=_('Image'), null=True, blank=True,
        upload_to=set_speaker_image_upload_path
    )

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')
        ordering = ('order_id', 'first_name', 'last_name')
        unique_together = ('first_name', 'last_name')

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Speaker, self).save(*args, **kwargs)
            self.image = saved_image

        return super(Speaker, self).save(*args, **kwargs)

    def __str__(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )

    def get_full_name(self):
        return self.__str__()

    def image_prev(self):
        if self.image:
            return '<img src="/media/%s" style="max-height: 200px; ' \
                   'background-color:rgba(0, 0, 0, 0.1);"/>' % (self.image)
        else:
            return _('Not Found!')
    image_prev.short_description = _('Preview')
    image_prev.allow_tags = True

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


class SpeakerSocialAccount(DateModel, SortableMixin):
    url = models.URLField(verbose_name=_('URL'))
    speaker = models.ForeignKey(verbose_name=_('Speaker'), to=Speaker)
    account = models.ForeignKey(verbose_name=_('Account'), to=SocialAccount)

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Speaker Social Account')
        verbose_name_plural = _('Speaker Social Accounts')
        ordering = ('order_id',)
        unique_together = ('speaker', 'account')

    def __str__(self):
        return '{speaker} - {account}'.format(
            speaker=self.speaker.__str__(), account=self.account.__str__()
        )
