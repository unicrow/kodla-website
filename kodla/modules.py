# Django
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# Local Django
from kodla.tasks import mail_task


class MailModule(object):

    @staticmethod
    def send_contact_mail(contact, user, domain=None):
        if not domain:
            domain = settings.DOMAIN

        template_context = {
            'domain': domain,
            'username': user.username,
            'contact_url': domain + reverse(
                'admin:form_contact_change', args=[contact.id]
            )
        }
        context = {
            'subject': _('New Contact'),
            'message': _(
                "Kodla\n"
                "Hello, {username}\n"
                "See Detail = {contact_url}\n").format(
                    username=template_context.get('username', ''),
                    contact_url=template_context.get('contact_url', '')
                ),
            'html_message': render_to_string(
                'mail/contact-mail.html', template_context
            ),
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [user.email]
        }

        mail_task.delay(context, 'contact')
