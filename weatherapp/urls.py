from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete/$', views.delete_elements, name='delete_elements'),
    url(r'^description/$', views.description, name='description'),
    url(r'^temperature/$', views.temperature, name='temperature'),
]
