# Third-Party
import collections

# Django
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

# Local Django
from form.forms import ContactForm
from activity.models import Activity


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, year=None, *args, **kwargs):
        self.activities = Activity.objects.filter(is_active=True)

        if not year:
            self.activity = self.activities.first()
        else:
            try:
                self.activity = Activity.objects.get(year=year)
            except (ValueError, Activity.DoesNotExist) as e:
                self.activity = None

        if not self.activity and year:
            return redirect('index')

        return super(IndexView, self).dispatch(request, year, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if self.activity:
            activity_timeline = collections.OrderedDict()
            for program in self.activity.program_set.filter(is_active=True):
                activity_timeline.update({
                    program: program.programcontent_set.filter(is_active=True)
                })

            activity_speakers = collections.OrderedDict()
            for speaker in self.activity.speakers.filter(is_active=True):
                activity_speakers.update({
                    speaker: speaker.speakersocialaccount_set.filter(
                        is_active=True
                    )
                })

            activity_sponsors = collections.OrderedDict()
            sponsors = self.activity.activitysponsor_set \
                .filter(is_active=True, sponsor_type__is_active=True) \
                .order_by('sponsor_type', 'order_id')
            for sponsor in sponsors:
                activity_sponsors.setdefault(sponsor.sponsor_type.name, []) \
                    .append(sponsor)

            context.update({
                'title': self.activity.short_description,
                'activity': self.activity,
                'activities': self.activities,
                'activity_document': self.activity.activitydocument_set \
                    .filter(is_active=True).first(),
                'activity_map': self.activity.activitymap_set \
                    .filter(is_active=True).first(),
                'activity_map_key': settings.GOOGLE_MAP_API_KEY,
                'activity_social_accounts': self.activity \
                    .activitysocialaccount_set.filter(is_active=True),
                'activity_speakers': activity_speakers,
                'activity_timeline': activity_timeline,
                'activity_sponsors': activity_sponsors,
                'contact_form': ContactForm()
            })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        contact_form = ContactForm(self.request.POST)

        if contact_form.is_valid() and self.activity:
            contact = contact_form.save(self.activity)

            if contact:
                messages.success(
                    request, _('Your message has been sent. Thank you.')
                )

                return HttpResponseRedirect(request.path)

        messages.error(request, _('Your message could not be sent. Try again.'))
        context.update({ 'contact_form': contact_form })

        return super(IndexView, self).render_to_response(context)
