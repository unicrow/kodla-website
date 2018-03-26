# Third-Party
from import_export import fields
from import_export import resources

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from form.models import Register


class RegisterResource(resources.ModelResource):
    first_name = fields.Field(column_name=_('First Name'))
    last_name = fields.Field(column_name=_('Last Name'))
    email = fields.Field(attribute='email', column_name=_('Email'))
    phone_number = fields.Field(
        attribute='phone_number', column_name=_('Phone Number')
    )
    tshirt_size = fields.Field(
        attribute='get_tshirt_size_display', column_name=_('T-shirt Size')
    )
    is_active = fields.Field(column_name=_('Active'))
    is_completed = fields.Field(column_name=_('Completed'))

    class Meta:
        model = Register
        fields = (
            'first_name', 'last_name', 'email', 'phone_number',
            'tshirt_size', 'is_active', 'is_completed'
        )
        export_order = fields

    def dehydrate_first_name(self, obj):
        return obj.first_name.title()

    def dehydrate_last_name(self, obj):
        return obj.last_name.title()

    def dehydrate_is_active(self, obj):
        return '+' if obj.is_active else ''

    def dehydrate_is_completed(self, obj):
        return '+' if obj.is_completed else ''
