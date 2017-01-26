from django.conf.urls import include, url
from django.contrib import admin
from weatherapp import views as weatherViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('weatherapp.urls')),

]
