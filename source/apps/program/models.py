# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel
from speaker.models import Speaker
from activity.models import Activity


class Program(DateModel):
    date = models.DateField(verbose_name=_('Date'))
    activity = models.ForeignKey(verbose_name=_('Activity'), to=Activity)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')
        ordering = ('activity', 'date')

    def __str__(self):
        return '{activity} - {date}'.format(
            activity=self.activity.__str__(), date=self.date.strftime("%d.%m.%Y")
        )


class ProgramContent(DateModel):
    subject = models.CharField(
        verbose_name=_('Subject'), max_length=255, null=True, blank=True
    )
    annotation = models.CharField(
        verbose_name=_('Annotation'), max_length=255, null=True, blank=True
    )
    start_time = models.TimeField(verbose_name=_('Start Time'))
    end_time = models.TimeField(
        verbose_name=_('End Time'), null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    program = models.ForeignKey(verbose_name=_('Program'), to=Program)
    speakers = models.ManyToManyField(
        verbose_name=_('Speaker'), to=Speaker, blank=True
    )

    class Meta:
        verbose_name = _('Program Content')
        verbose_name_plural = _('Program Contents')
        ordering = ('program', 'start_time')

    def __str__(self):
        return '{subject}-{annotation}'.format(
            subject=self.subject, annotation=self.annotation
        ).strip('-')

    def get_speakers(self):
        speakers_name = [
            speaker.get_full_name() for speaker in self.speakers.filter(
                is_active=True
            )
        ]

        return ', '.join(speakers_name)
