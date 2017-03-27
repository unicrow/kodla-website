# Third-Party
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

# Django
from django import forms
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import SocialAccount
from speaker.models import SpeakerApplicationType, SpeakerApplication



class SpeakerApplicationForm(forms.ModelForm):
    application_type = forms.ModelChoiceField(
        label=_('Application Type'), required=True,
        queryset=SpeakerApplicationType.objects.filter(is_active=True)
    )
    first_name = forms.CharField(label=_('Your Name'), max_length=50)
    last_name = forms.CharField(label=_('Your Surname'), max_length=50)
    email = forms.EmailField(label=_('E-Mail Address'), required=True)
    image = forms.ImageField(label=_('Your Image'), required=True)
    company= forms.CharField(
        label=_('Your working company'), max_length=255, required=False
    )
    position = forms.CharField(
        label=_('Your working position'), max_length=255, required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Frontend Developer, Backend Developer, etc.'
        })
    )
    website = forms.URLField(label=_('Your Website/Your Blog'), required=False)
    twitter = forms.URLField(
        label=_('Your Twitter Account'), required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'https://twitter.com/username'
        })
    )
    github = forms.URLField(
        label=_('Your Github Account'), required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'https://github.com/username'
        })
    )
    linkedin = forms.URLField(
        label=_('Your Linkedin Account'), required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'https://linkedin.com/in/username'
        })
    )
    other_social_account = forms.URLField(
        label=_('Your Other Social Account'), required=False,
        widget=forms.TextInput(attrs={
            'placeholder': _(
                'You Can Enter If You Have Another Social Media Account'
            )
        })
    )
    note = forms.CharField(
        label=_('Your Note'), required=False, widget=forms.Textarea
    )
    recaptcha = ReCaptchaField(widget=ReCaptchaWidget(explicit=True))

    class Meta:
        model = SpeakerApplication
        fields = (
            'application_type', 'email', 'first_name', 'last_name', 'company',
            'position', 'image', 'website', 'twitter', 'github', 'linkedin',
            'other_social_account', 'note', 'recaptcha'
        )

    def save(self, activity=None, commit=True):
        speaker_application = super(SpeakerApplicationForm, self).save(
            commit=False
        )
        created = False

        if commit and activity:
            try:
                speaker_application = SpeakerApplication.objects.get(
                    application_type=self.cleaned_data.get('application_type'),
                    first_name=self.cleaned_data.get('first_name'),
                    last_name=self.cleaned_data.get('last_name'),
                    activity=activity
                )
            except SpeakerApplication.DoesNotExist:
                speaker_application = SpeakerApplication(
                    application_type = self.cleaned_data.get('application_type'),
                    email = self.cleaned_data.get('email'),
                    first_name=self.cleaned_data.get('first_name'),
                    last_name=self.cleaned_data.get('last_name'),
                    company = self.cleaned_data.get('company'),
                    position = self.cleaned_data.get('position'),
                    image = self.cleaned_data.get('image'),
                    website = self.cleaned_data.get('website'),
                    twitter = self.cleaned_data.get('twitter'),
                    github = self.cleaned_data.get('github'),
                    linkedin = self.cleaned_data.get('linkedin'),
                    other_social_account = self.cleaned_data.get(
                        'other_social_account'
                    ),
                    note = self.cleaned_data.get('note'),
                    activity=activity
                )
                speaker_application.save()
                created = True

        return speaker_application, created
