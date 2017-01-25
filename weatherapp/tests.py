from django.test import TestCase
from weatherapp.models import Weather

# Create your tests here.
#w= Weather(temperature=k_to_c(json_response["main"]["temp"]),zipcode=ciudad, description=json_response["weather"][0]["description"], sunrise= json_response["sys"]["sunrise"], sunset= json_response["sys"]["sunset"],wind= json_response["wind"]["speed"])

class Weather(TestCase):

    def CreateWeather(self):
        Weather.objects.create(temperature='35',zipcode='grandada', description='Cloudy', sunrise= '2017-01-25 07:21:56', sunset= '2017-01-25 07:21:56',wind= '4.6')
