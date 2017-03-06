# Django
from django import template


register = template.Library()


@register.simple_tag
def add_attrs(field, **kwargs):
    attr_names = kwargs.keys()

    for attr_name in attr_names:

        field.field.widget.attrs.update({
            attr_name.replace("_", "-"):kwargs[attr_name]
            })

    return field
