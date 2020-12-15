from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'', views.base_view, name='income_base_view'),
    url(r'^incomes$', views.incomes_list, name='incomes_list'),
    url(r'^income/(?P<pk>[0-9]+)/$',
        views.income_detail, name='income_detail'),
    url(r'^income/new/$', views.income_new, name='income_new'),
    url(r'^income/(?P<pk>[0-9]+)/edit/$',
        views.income_edit, name='income_edit'),
]
