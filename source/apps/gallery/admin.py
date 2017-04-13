# Third-Party
from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableStackedInline

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from gallery.models import Gallery, GalleryContent


class GalleryContentInline(SortableStackedInline):
    model = GalleryContent
    extra = 6
    max_num = 6
    min_num = 6
    verbose_name = _('Gallery Content')
    verbose_name_plural = _('Gallery Contents')
    readonly_fields = ('create_date', 'update_date', 'image_prev')
    fields = (('image', 'image_prev'),)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Gallery)
class GalleryAdmin(SortableAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = ('activity', 'name', 'tag', 'show_url', 'is_active')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    inlines = (GalleryContentInline,)
