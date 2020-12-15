from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'costs$', views.costs_list, name='costs_list'),
    url(r'^cost/(?P<pk>[0-9]+)/$',
        views.cost_detail, name='cost_detail'),
    url(r'^cost/new/$', views.cost_new, name='cost_new'),
    url(r'^cost/(?P<pk>[0-9]+)/edit/$',
        views.cost_edit, name='cost_edit'),
]
