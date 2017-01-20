from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^zipcode/$', views.zipcode_get, name='zipcode_get'),
    url(r'^zipcode/(?P<zipcode>\w+)/$', csrf_exempt(views.zipcode_post), name='zipcode_post'),
    url(r'^description/$', views.description, name='description'),
    url(r'^temperature/$', views.temperature, name='temperature')
]
