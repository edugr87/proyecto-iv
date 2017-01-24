from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^description/$', views.description, name='description'),
    url(r'^temperature/$', views.temperature, name='temperature'),
]
