from django.urls import re_path, path
from events.views import (
    EventDetailView,
    EventsListView,
    LocationDetailView,
    LocationsListView,
    EventInviteDownloadView,
)
from events.feeds import Calendar

slug = '(?P<slug>[-\\w\\d]+)'
pk = '(?P<pk>[0-9]+)'
date = '(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})'
event_path = f'{date}/{slug}/{pk}/$'

urlpatterns = [
    # location
    path('location/<slug:slug>/<int:pk>/', LocationDetailView.as_view(), name='location'),
    path('locations/', LocationsListView.as_view(), name='locations'),

    # event
    re_path(r'^{}'.format(event_path), EventDetailView.as_view(), name='event'),
    path('invite/<int:pk>/', EventInviteDownloadView.as_view(), name='event-invite'),
    path('', EventsListView.as_view(), name='events'),

    # calendar
    path('feed/ical/', Calendar(), name='calendar'),
]
