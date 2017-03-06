# Django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FormConfig(AppConfig):
    name = 'form'
    verbose_name = _('Form')
