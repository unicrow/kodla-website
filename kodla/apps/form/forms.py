# Third-Party
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

# Django
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Local Django
from kodla.modules import MailModule
from form.models import Contact, Register


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(label=_('Name and Surname'), max_length=100)
    email = forms.EmailField(label=_('Email Address'))
    message = forms.CharField(label=_('Your Message'), widget=forms.Textarea)
    recaptcha = ReCaptchaField(widget=ReCaptchaWidget(explicit=True))

    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'message', 'recaptcha')

    def save(self, activity=None, request=None, commit=True):
        contact = super(ContactForm, self).save(commit=False)

        if commit and activity:
            try:
                contact = Contact(
                    full_name=self.cleaned_data.get('full_name'),
                    email=self.cleaned_data.get('email'),
                    message=self.cleaned_data.get('message'),
                    activity=activity
                )

                contact.save()

                # Send Contact Mail
                domain = request.META.get('HTTP_ORIGIN', None)
                users = User.objects.filter(is_superuser=True)
                for user in users:
                    MailModule.send_contact_mail(contact, user, domain)
            except:
                contact = None

        return contact


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label=_('Your Name'), max_length=100)
    last_name = forms.CharField(label=_('Your Surname'), max_length=100)
    email = forms.EmailField(label=_('Email Address'))
    phone_number = forms.CharField(label=_('Phone Number'), required=True)
    recaptcha = ReCaptchaField(widget=ReCaptchaWidget(explicit=True))

    class Meta:
        model = Register
        fields = (
            'first_name', 'last_name', 'email',
            'phone_number', 'tshirt_size', 'recaptcha'
        )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['tshirt_size'].required = True

    def save(self, activity=None, commit=True):
        register = super(RegisterForm, self).save(commit=False)
        created = False

        if commit and activity:
            try:
                register = Register.objects.get(
                    email=self.cleaned_data.get('email'),
                    activity=activity
                )
            except Register.DoesNotExist:
                register = Register(
                    first_name=self.cleaned_data.get('first_name'),
                    last_name=self.cleaned_data.get('last_name'),
                    email=self.cleaned_data.get('email'),
                    phone_number=self.cleaned_data.get('phone_number'),
                    tshirt_size=self.cleaned_data.get('tshirt_size'),
                    activity=activity
                )
                register.save()
                created = True
            except Register.MultipleObjectsReturned:
                pass

        return register, created
