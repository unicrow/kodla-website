# Django
from django.shortcuts import redirect
from django.views.generic import TemplateView

# Local Django
from activity.models import Activity


class IndexView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, year=None, *args, **kwargs):
        if not year:
            self.activity = Activity.objects.first()
        else:
            try:
                self.activity = Activity.objects.filter(year=year).first()
            except:
                pass

        if not self.activity:
            return redirect('index')

        return super(IndexView, self).dispatch(request, year, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if self.activity:
            context.update({
                'title': self.activity.short_description,
                'activity': self.activity
            })

        return context
