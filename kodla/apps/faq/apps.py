from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class FaqConfig(AppConfig):
    name = 'faq'
    verbose_name = _('FAQ')
