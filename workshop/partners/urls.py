from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^partners/$', views.partners_list, name='partners'),
    url(r'^partners/new$', views.partner_new, name='partner_new'),
    url(r'^partners/edit/(?P<pk>[0-9]+)/$',
        views.partner_edit,
        name='partner_edit'
        ),
]
