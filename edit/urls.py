from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^protocol/(?P<protocol_id>\d+)$', views.get_protocol),
	url(r'^paradigm/(?P<paradigm_id>\d+)/actions$', views.actions_list),
	url(r'^protocol/(?P<protocol_id>\d+)/events$', views.events_list),
	url(r'^protocol/(?P<protocol_id>\d+)/intervals$',views.intervals_list),
	url(r'^protocol/(?P<protocol_id>\d+)/intervals/view$',views.intervals_listview),
	url(r'^paradigm/(?P<paradigm_id>\d+)/make_protocol$',views.make_protocol),
	url(r'^protocol/(?P<protocol_id>\d+)/set_trial_duration$', views.set_trial_duration),
	url(r'^protocol/(?P<protocol_id>\d+)/new_interval$', views.new_interval),
	url(r'^interval/(?P<interval_id>\d+)/edit$', views.edit_interval),
	url(r'^interval/(?P<interval_id>\d+)/delete', views.delete_interval),
	url(r'^protocol/(?P<protocol_id>\d+)/new_event$', views.new_event),
	url(r'^event/(?P<event_id>\d+)/edit$', views.edit_event),
)