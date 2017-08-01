from django.conf.urls import url

from remote_control.views import receive_request

urlpatterns = [
    url(r'^$', receive_request)
]
