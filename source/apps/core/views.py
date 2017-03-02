# Third-Party
import collections

# Django
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import TemplateView

# Local Django
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
            timeline = collections.OrderedDict()
            for program in self.activity.program_set.filter(is_active=True):
                timeline.update({
                    program: program.programcontent_set.filter(is_active=True)
                })

            speakers = collections.OrderedDict()
            for speaker in self.activity.speakers.filter(is_active=True):
                speakers.update({
                    speaker: speaker.speakersocialaccount_set.filter(is_active=True)
                })

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
                'speakers': speakers,
                'timeline': timeline
            })

        return context
