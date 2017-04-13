# Third-Party
from adminsortable.models import SortableMixin

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import DateModel


class Gallery(DateModel, SortableMixin):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    tag = models.CharField(verbose_name=_('Tag'), max_length=100)
    url = models.URLField(verbose_name=_('URL'), max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    activity = models.ForeignKey(
        verbose_name=_('Activity'), to='activity.Activity'
    )

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')
        ordering = ('order_id', 'activity', 'name')

    def __str__(self):
        return '{activity} - {name}'.format(
        	activity=self.activity.__str__(), name=self.name
        )

    def show_url(self):
        if self.url:
            return "<a href='%s' target='_blank'>%s</a>" % (
                self.url, self.url
            )

        return self.url
    show_url.allow_tags = True
    show_url.short_description = _('URL')


def set_gallerycontent_images_upload_path(instance, filename):
    return '/'.join([
        'gallery', 'gallery_%d' % instance.gallery.id,
        'contents', 'content_%d' % instance.id, 'image', filename
    ])


class GalleryContent(DateModel, SortableMixin):
    image = models.ImageField(
        verbose_name=_('Image'), upload_to=set_gallerycontent_images_upload_path
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    gallery = models.ForeignKey(
        verbose_name=_('Gallery'), to='gallery.Gallery'
    )

    # ordering field
    order_id = models.PositiveSmallIntegerField(
        default=0, editable=False, db_index=True
    )

    class Meta:
        verbose_name = _('Gallery Content')
        verbose_name_plural = _('Gallery Contents')
        ordering = ('order_id', 'gallery')

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(GalleryContent, self).save(*args, **kwargs)
            self.image = saved_image

        return super(GalleryContent, self).save(*args, **kwargs)

    def __str__(self):
        return '{image}...'.format(image=str(self.image.name).split('/')[-1])

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