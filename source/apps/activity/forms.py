# Third-Party
from redactor.widgets import RedactorEditor

# Django
from django import forms

# Local Django
from activity.models import Activity


class ActivityAdminForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
           'description': RedactorEditor(),
           'address': RedactorEditor(),
           'transportation': RedactorEditor(),
           'accommodation': RedactorEditor(),
        }
