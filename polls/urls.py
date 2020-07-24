from django.urls import path

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^vendas/$', views.VendasList.as_view(), name='vendas-list'),
    path('insert/<int:id>', views.insert, name='insert'),
    url(r'^vendas/(?P<pk>[0-9]+)/$', views.VendasDetail.as_view(), name='vendas-detail'),
]
