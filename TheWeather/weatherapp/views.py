from django.http import HttpResponse, JsonResponse
import datetime, requests, json
from django.shortcuts import render
from django.template import loader
from models import Weather
from datetime import datetime
from forms import SearchForm

weather_url="http://api.openweathermap.org/data/2.5/weather?q={},es&appid=ceb51408067b2e840e12f34c8c82d1cb"


def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>son las %s.</body></html>" %now
    return HttpResponse(html)

#Kelvin to Farenheit
def k_to_c(kelvin):
    return round(kelvin-273.15)

#  Get zipcode from the database
def index(request):

    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            url=weather_url.format(request.POST['ciudad'])
            ciudad=request.POST['ciudad']
            toDel = Weather.objects.filter(zipcode=ciudad)
            toDel.delete()
            response = requests.get(url)

            json_response = json.loads(response.text)

            w= Weather(temperature=k_to_c(json_response["main"]["temp"]),zipcode=ciudad, description=json_response["weather"][0]["description"], sunrise= datetime.utcfromtimestamp(json_response["sys"]["sunrise"]), sunset= datetime.utcfromtimestamp(json_response["sys"]["sunset"]),wind= json_response["wind"]["speed"])
            w.save()
            #html="<html><body>%s y %s</body></html>"% (w.temperature, w.zipcode)
            context_dict = {}
            context_dict['temperature'] = k_to_c(json_response["main"]["temp"])
            context_dict['zipcode'] = ciudad
            context_dict['description'] = json_response["weather"][0]["description"]
            context_dict['sunrise']= datetime.utcfromtimestamp(json_response["sys"]["sunrise"])
            context_dict['sunset']= datetime.utcfromtimestamp(json_response["sys"]["sunset"])
            context_dict['wind']= json_response["wind"]["speed"]

            return render(request, 'weather/weather.html', context_dict)
    else:
        w= Weather.objects.all()
        context_dict = {'city': w,'form':SearchForm()}

        return render(request, 'weather/index.html', context_dict)

# If method is post create the resources needed for zipcdode under id=1
def zipcode_post(request):
    #return HttpResponse("Hello Weather")
    if (request.method == "POST"):
        form = SearchForm(request.POST)
        if form.is_valid():
            url=weather_url.format(request.POST['ciudad'])
            response = requests.get(url)

            json_response = json.loads(response.text)

            w= Weather(temperature=k_to_c(json_response["main"]["temp"]),zipcode=zipcode, description=json_response["weather"][0]["description"], sunrise= json_response["sys"]["sunrise"], sunset= json_response["sys"]["sunset"],wind= json_response["wind"]["speed"])
            w.save()
            #html="<html><body>%s y %s</body></html>"% (w.temperature, w.zipcode)
            context_dict = {}
            context_dict['temperature'] = k_to_c(json_response["main"]["temp"])
            context_dict['zipcode'] = zipcode
            context_dict['description'] = json_response["weather"][0]["description"]
            context_dict['sunrise']= datetime.utcfromtimestamp(json_response["sys"]["sunrise"])
            context_dict['sunset']= datetime.utcfromtimestamp(json_response["sys"]["sunset"])
            context_dict['wind']= json_response["wind"]["speed"]

            return render(request, 'weather/weather.html', context_dict)

#return the decription in the db
def description(request):
    w= Weather.objects.get(id=1)
    return HttpResponse(w.description)

#return the description of the temp in the db
def temperature(request):
    w= Weather.objects.get(id=1)
    return HttpResponse(w.temperature)
