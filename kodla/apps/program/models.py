# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


class Program(DateModel):
    date = models.DateField(verbose_name=_('Date'))
    title = models.CharField(
        verbose_name=_('Title'), max_length=255, null=True, blank=True
    )
    description = models.TextField(verbose_name=_('Description'), blank=True)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')
        ordering = ('activity', 'date')

    def __str__(self):
        return '{activity} - {date}'.format(
            activity=self.activity.__str__(), date=self.date.strftime("%d.%m.%Y")
        )


def set_programcontent_documents_upload_path(instance, filename):
    return '/'.join([
        'programs', 'program_%d' % instance.program.id,
        'contents', 'content_%d' % instance.id, 'presentation', filename
    ])


class ProgramContent(DateModel):
    subject = models.CharField(
        verbose_name=_('Subject'), max_length=255, null=True, blank=True
    )
    annotation = models.CharField(
        verbose_name=_('Annotation'), max_length=255, null=True, blank=True
    )
    presentation_url = models.URLField(
        verbose_name=_('Presentation URL'), null=True, blank=True
    )
    presentation_document = models.FileField(
        verbose_name=_('Presentation Document'), null=True, blank=True,
        upload_to=set_programcontent_documents_upload_path
    )
    start_time = models.TimeField(verbose_name=_('Start Time'))
    end_time = models.TimeField(
        verbose_name=_('End Time'), null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    program = models.ForeignKey(
        verbose_name=_('Program'), to='program.Program'
    )
    speakers = models.ManyToManyField(
        verbose_name=_('Speaker'), to='speaker.Speaker', blank=True
    )

    class Meta:
        verbose_name = _('Program Content')
        verbose_name_plural = _('Program Contents')
        ordering = ('program', 'start_time')

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_presentation_document = self.presentation_document
            self.presentation_document = None
            super(ProgramContent, self).save(*args, **kwargs)
            self.presentation_document = saved_presentation_document

        return super(ProgramContent, self).save(*args, **kwargs)

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
