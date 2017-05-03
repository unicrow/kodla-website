# Third-Party
from redactor.widgets import RedactorEditor

# Django
from django import forms
from django.utils.translation import ugettext_lazy as _

# Local Django
from hackathon.models import Hackathon, HackathonPrize


class HackathonAdminForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = '__all__'
        widgets = {
           'description': RedactorEditor(),
        }

    def check_hackathon(self, activity):
        try:
            hackathon = Hackathon.objects.get(activity=activity)

            if self.instance.pk == hackathon.pk:
                hackathon = None
        except Hackathon.DoesNotExist:
            hackathon = None

        return hackathon

    def clean_activity(self):
        activity = self.cleaned_data['activity']
        hackathon = self.check_hackathon(activity)

        if hackathon:
            raise forms.ValidationError(_('Activity hackathon already exist.'))

        return self.cleaned_data['activity']


class HackathonPrizeAdminForm(forms.ModelForm):
    class Meta:
        model = HackathonPrize
        fields = '__all__'
        widgets = {
           'description': RedactorEditor(),
        }

