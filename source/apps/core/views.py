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
            context.update({
                'title': self.activity.short_description,
                'activity': self.activity,
                'activities': self.activities,
                'activity_map': self.activity.activitymap_set.first(),
                'activity_map_key': settings.GOOGLE_MAP_API_KEY,
                'speakers': self.activity.speakers.filter(is_active=True)
            })

        return context
