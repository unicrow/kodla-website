# Django
from django.core.mail import send_mail

# Local Django
from kodla import celery_app


@celery_app.task
def mail_task(context, verb):
    """
    Context Format
        context = {
            subject="subject"
            message="messages"
            html_message=render_to_string('email/email.html', template_context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        }
    """

    try:
        send_mail(**context)

        return ','.join(context['recipient_list']) + ' success = ' + verb
    except:
        return ','.join(context['recipient_list']) + ' error = ' + verb
