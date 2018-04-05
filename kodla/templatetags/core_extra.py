# Django
from django import template

# Local Django
from kodla.variables import (
    CONTACT_FORM_PREFIX, SPEAKER_APPLICATION_FORM_PREFIX, REGISTER_FORM_PREFIX
)


register = template.Library()


@register.simple_tag
def add_attrs(field, **kwargs):
    attr_names = kwargs.keys()

    for attr_name in attr_names:

        field.field.widget.attrs.update({
            attr_name.replace("_", "-"):kwargs[attr_name]
            })

    return field


@register.filter(name='iternum')
def iternum(num):
    return range(num)


@register.filter(name='active_form')
def active_form(activity, request):
	if REGISTER_FORM_PREFIX in request.POST:
		return REGISTER_FORM_PREFIX

	if SPEAKER_APPLICATION_FORM_PREFIX in request.POST:
		return SPEAKER_APPLICATION_FORM_PREFIX

	if CONTACT_FORM_PREFIX in request.POST:
		return CONTACT_FORM_PREFIX

	if activity.has_register:
		return REGISTER_FORM_PREFIX
	elif activity.has_speaker_application:
		return SPEAKER_APPLICATION_FORM_PREFIX
	else:
		return CONTACT_FORM_PREFIX
