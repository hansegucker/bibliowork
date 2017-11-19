from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /biblio/
    url(r'^$', views.index, name='index'),
    # ex: /biblio/1/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/1/edit/
    url(r'^(?P<book_id>[0-9]+)/edit/$', views.edit, name='edit'),
]
