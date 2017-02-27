# Third-Party
from geoposition.fields import GeopositionField

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Activity(models.Model):
    year = models.PositiveSmallIntegerField(verbose_name=_('Year'))
    logo = models.TextField(
        verbose_name=_('Logo'), null=True, blank=True
    )
    meta_tags = models.TextField(
        verbose_name=_('Meta Tags'), null=True, blank=True
    )
    short_description = models.CharField(
        verbose_name=_('Short Description'),
        max_length=500, null=True, blank=True
    )
    description = models.TextField(
        verbose_name=_('Description'), null=True, blank=True
    )
    register_url = models.URLField(
        verbose_name=_('Register URL'), null=True, blank=True
    )

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')
        ordering = ('-year',)

    def __str__(self):
        return "{year}".format(year=self.year)

    def show_register_url(self):
        if self.register_url:
            return "<a href='%s' target='_blank'>%s</a>" % (self.register_url, self.register_url)

        return self.register_url
    show_register_url.allow_tags = True
    show_register_url.short_description = _('Register URL')


class ActivityMap(models.Model):
    description = models.CharField(
        verbose_name=_('Description'), max_length=250, null=True, blank=True
    )
    coordinates = GeopositionField(verbose_name=_('Coordinates'))
    activity = models.ForeignKey(verbose_name=_('Activity'), to=Activity)

    class Meta:
        verbose_name = _('Activity Map')
        verbose_name_plural = _('Activity Maps')
        ordering = ('activity',)


def set_activity_upload_path(instance, filename):
    return '/'.join(
        ['activity', str(instance.activity.id), 'sponsor_docs', filename]
    )


class ActivityDocument(models.Model):
    document = models.FileField(
        verbose_name=_('Document'), upload_to=set_activity_upload_path
    )
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to=Activity, related_name='activity_documents'
    )

    class Meta:
        verbose_name = _('Activity Document')
        verbose_name_plural = _('Activity Documents')

    def get_document_name(self):
        return str(self.document.file).split('/')[-1]

    def get_size(self):
        return self.document._get_size()

    get_size.short_description =  _('Size')

    def get_size_humanize(self):
        num = self.get_size()
        for unit in ['B','KB','MB','GB','TB','PB','EB','ZB']:
            if abs(num) < 1024.0:
                return '%3.1f%s' % (num, unit)

            num /= 1024.0
        return '%.1f%s%s' % (num, 'Y')

    get_size_humanize.short_description =  _('Size(Humanize)')

    def download_document_link(self):
        if self.document:
            return "<a href='%s' download>%s</a>" % (self.document.url, self.get_document_name())
        else:
            return _('Document not found!')
    download_document_link.allow_tags = True
    download_document_link.short_description = _('Download')

    def show_document_link(self):
        if self.document:
            return "<a href='%s' target='_blank'>%s</a>" % (self.document.url, self.get_document_name())
        else:
            return _('Document not found!')
    show_document_link.allow_tags = True
    show_document_link.short_description = _('Show')

    def __str__(self):
        return '{document_name}'.format(document_name=self.get_document_name())
