from django.conf.urls import include, url
from . import views

app_name = 'board'
urlpatterns = [             #name value -> {% url %}에서 불러낼 때 쓰임!
                            #ex /polls/             ...$ = 끝
    url(r'^$', views.indexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.postView.as_view(), name='post'),
    url(r'^writing/$', views.writing, name='writing'),
    url(r'^submit/$', views.submit, name='subit'),
    url(r'^(?P<post_id>[0-9]+)/talkSubmit/$', views.talkSubmit, name='talkSubit'),
    url(r'^hit/$', views.hit, name='hit'),
    url(r'^modify/$', views.modify, name='modify'),
    url(r'^modiSubmit/$', views.modiSubmit, name='modiSubmit'),
]
