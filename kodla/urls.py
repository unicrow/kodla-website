"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# Third-Party
from rest_framework import routers

# Django
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include

# Local Django
from activity.api_views import ActivityViewSet
from kodla.views import get_tweets, IndexView, HackathonView


router = routers.DefaultRouter()
router.register('activities', ActivityViewSet, 'activities')


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include(router.urls)),

    # Editor
    url(r'^redactor/', include('redactor.urls')),

    # Pages
    url(r'^hackathon/$', HackathonView.as_view(), name='hackathon'),
    url(
        r'^(?P<year>\w+)?/hackathon/$',
        HackathonView.as_view(), name='hackathon-year'
    ),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<year>\w+)?/$', IndexView.as_view(), name='index-year'),
    url(r'^get-tweets/$', get_tweets, name='get-tweets')
]


# Media
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
