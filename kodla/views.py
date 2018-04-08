# Standart Library
import json

# Third-Party
import twitter
import collections
from ttp import ttp

# Django
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

# Local Django
from activity.models import Activity
from form.forms import ContactForm, RegisterForm
from speaker.forms import SpeakerApplicationForm
from kodla.variables import (
    CONTACT_FORM_PREFIX, SPEAKER_APPLICATION_FORM_PREFIX,
    REGISTER_FORM_PREFIX, DEFAULT_PROGRAM_CONTENTS
)


def get_tweets(request):
    datas = []
    p = ttp.Parser()

    try:
        api = twitter.Api(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_ACCESS_TOKEN,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
        )

        tweets = api.GetUserTimeline(screen_name='kodlaco')
        for tweet in tweets:
            datas.append({
                #'text': p.parse(tweet.text).html,
                'text': tweet.text,
                'id_str': tweet.id_str
            })
    except:
        datas = []

    return HttpResponse(json.dumps(datas), content_type="application/json")


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

            if self.activity and self.activity == self.activities.first():
                return redirect('index')

        if not self.activity and year:
            return redirect('index')

        return super(IndexView, self).dispatch(request, year, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if self.activity:
            activity_galleries = collections.OrderedDict()
            for gallery in self.activity.gallery_set.filter(is_active=True):
                activity_galleries.update({
                    gallery: gallery.gallerycontent_set.filter(is_active=True)
                })

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
                'hackathon': self.activity.hackathon_set.filter(is_active=True),
                'activity_document': self.activity.activitydocument_set \
                    .filter(is_active=True).first(),
                'activity_map': self.activity.activitymap_set \
                    .filter(is_active=True).first(),
                'activity_map_key': settings.GOOGLE_MAPS_API_KEY,
                'activity_social_accounts': self.activity \
                    .activitysocialaccount_set.filter(is_active=True),
                'activity_galleries': activity_galleries,
                'activity_timeline': activity_timeline,
                'activity_speakers': activity_speakers,
                'default_program_contents': DEFAULT_PROGRAM_CONTENTS,
                'activity_sponsors': activity_sponsors,
                'contact_form': ContactForm(prefix=CONTACT_FORM_PREFIX),
                'speaker_application_form': SpeakerApplicationForm(
                    prefix=SPEAKER_APPLICATION_FORM_PREFIX
                ),
                'register_form': RegisterForm(prefix=REGISTER_FORM_PREFIX)
            })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if CONTACT_FORM_PREFIX in request.POST:
            contact_form = ContactForm(request.POST, prefix=CONTACT_FORM_PREFIX)
            context.update({'contact_form': contact_form})

            if contact_form.is_valid() and self.activity:
                contact = contact_form.save(self.activity, request)

                if contact:
                    messages.success(
                        request, _('Your message has been sent. Thank you.')
                    )
                    context.update({
                        'contact_form': ContactForm(prefix=CONTACT_FORM_PREFIX)
                    })

                    return super(IndexView, self).render_to_response(context)

            messages.error(
                request, _('Your message could not be sent. Try again.')
            )

        if SPEAKER_APPLICATION_FORM_PREFIX in request.POST:
            speaker_application_form = SpeakerApplicationForm(
                request.POST, request.FILES,
                prefix=SPEAKER_APPLICATION_FORM_PREFIX
            )
            context.update({
                'speaker_application_form': speaker_application_form
            })

            if speaker_application_form.is_valid() and self.activity:
                speaker_application, created = speaker_application_form.save(
                    self.activity
                )

                if speaker_application:
                    if created:
                        messages.success(
                            request, _('Your application has been sent. Thank you.')
                        )

                        context.update({
                            'speaker_application_form': SpeakerApplicationForm(
                                prefix=SPEAKER_APPLICATION_FORM_PREFIX
                            )
                        })
                    else:
                        messages.error(
                            request, _('Your application already exists!')
                        )

                    return super(IndexView, self).render_to_response(context)

            messages.error(
                request, _('Your application could not be sent. Try again.')
            )

        if REGISTER_FORM_PREFIX in request.POST:
            register_form = RegisterForm(request.POST, prefix=REGISTER_FORM_PREFIX)
            context.update({
                'register_form': register_form
            })

            if register_form.is_valid() and self.activity:
                register, created = register_form.save(self.activity)

                if register:
                    if created:
                        messages.success(
                            request, _('Your register has been sent. Thank you.')
                        )

                        context.update({
                            'register_form': RegisterForm(
                                prefix=REGISTER_FORM_PREFIX
                            )
                        })
                    else:
                        messages.error(
                            request, _('Your register already exists!')
                        )

                    return super(IndexView, self).render_to_response(context)

            messages.error(
                request, _('Your register could not be sent. Try again.')
            )

        return super(IndexView, self).render_to_response(context)


class HackathonView(TemplateView):
    template_name = 'hackathon.html'

    def dispatch(self, request, year=None, *args, **kwargs):
        self.activities = Activity.objects.filter(is_active=True)

        if not year:
            self.activity = self.activities.first()
        else:
            try:
                self.activity = Activity.objects.get(year=year)
            except (ValueError, Activity.DoesNotExist) as e:
                self.activity = None

            if self.activity and self.activity == self.activities.first():
                return redirect('hackathon')

        if not self.activity and year:
            return redirect('index')

        self.hackathon = self.activity.hackathon_set.filter(
            activity=self.activity, is_active=True
        ).first()

        if not self.hackathon:
            return redirect('index')

        return super(HackathonView, self).dispatch(request, year, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HackathonView, self).get_context_data(**kwargs)

        if self.activity and self.hackathon:
            activity_sponsors = collections.OrderedDict()
            sponsors = self.activity.activitysponsor_set \
                .filter(is_active=True, sponsor_type__is_active=True) \
                .order_by('sponsor_type', 'order_id')
            for sponsor in sponsors:
                activity_sponsors.setdefault(sponsor.sponsor_type.name, []) \
                    .append(sponsor)

            context.update({
                'title': self.activity.short_description,
                'hackathon': self.hackathon,
                'hackathon_prizes': self.hackathon.hackathonprize_set\
                    .filter(is_active=True),
                'activity': self.activity,
                'activities': self.activities,
                'activity_document': self.activity.activitydocument_set \
                    .filter(is_active=True).first(),
                'activity_map': self.activity.activitymap_set \
                    .filter(is_active=True).first(),
                'activity_map_key': settings.GOOGLE_MAPS_API_KEY,
                'activity_social_accounts': self.activity \
                    .activitysocialaccount_set.filter(is_active=True),
                'activity_sponsors': activity_sponsors,
                'contact_form': ContactForm(prefix=CONTACT_FORM_PREFIX),
                'speaker_application_form': SpeakerApplicationForm(
                    prefix=SPEAKER_APPLICATION_FORM_PREFIX
                ),
                'register_form': RegisterForm(prefix=REGISTER_FORM_PREFIX)
            })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if CONTACT_FORM_PREFIX in request.POST:
            contact_form = ContactForm(request.POST, prefix=CONTACT_FORM_PREFIX)
            context.update({'contact_form': contact_form})

            if contact_form.is_valid() and self.activity:
                contact = contact_form.save(self.activity, request)

                if contact:
                    messages.success(
                        request, _('Your message has been sent. Thank you.')
                    )
                    context.update({
                        'contact_form': ContactForm(prefix=CONTACT_FORM_PREFIX)
                    })

                    return super(HackathonView, self).render_to_response(context)

            messages.error(
                request, _('Your message could not be sent. Try again.')
            )

        if SPEAKER_APPLICATION_FORM_PREFIX in request.POST:
            speaker_application_form = SpeakerApplicationForm(
                request.POST, request.FILES,
                prefix=SPEAKER_APPLICATION_FORM_PREFIX
            )
            context.update({
                'speaker_application_form': speaker_application_form
            })

            if speaker_application_form.is_valid() and self.activity:
                speaker_application, created = speaker_application_form.save(
                    self.activity
                )

                if speaker_application:
                    if created:
                        messages.success(
                            request, _('Your application has been sent. Thank you.')
                        )

                        context.update({
                            'speaker_application_form': SpeakerApplicationForm(
                                prefix=SPEAKER_APPLICATION_FORM_PREFIX
                            )
                        })
                    else:
                        messages.error(
                            request, _('Your application already exists!')
                        )

                    return super(HackathonView, self).render_to_response(context)

            messages.error(
                request, _('Your application could not be sent. Try again.')
            )

        if REGISTER_FORM_PREFIX in request.POST:
            register_form = RegisterForm(request.POST, prefix=REGISTER_FORM_PREFIX)
            context.update({
                'register_form': register_form
            })

            if register_form.is_valid() and self.activity:
                register, created = register_form.save(self.activity)

                if register:
                    if created:
                        messages.success(
                            request, _('Your register has been sent. Thank you.')
                        )

                        context.update({
                            'register_form': RegisterForm(
                                prefix=REGISTER_FORM_PREFIX
                            )
                        })
                    else:
                        messages.error(
                            request, _('Your register already exists!')
                        )

                    return super(HackathonView, self).render_to_response(context)

            messages.error(
                request, _('Your register could not be sent. Try again.')
            )

        return super(HackathonView, self).render_to_response(context)
