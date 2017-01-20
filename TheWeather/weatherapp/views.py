from django.http import HttpResponse, JsonResponse
import datetime, requests, json
from django.shortcuts import render
from models import Weather

weather_url="http://api.openweathermap.org/data/2.5/weather?q={},es&appid=ceb51408067b2e840e12f34c8c82d1cb"

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>son las %s.</body></html>" %now
    return HttpResponse(html)

#Kelvin to Farenheit
def k_to_f(kelvin):
    return round(kelvin*(9.0/5.0) - 459.67,2)

#  Get zipcode from the database
def zipcode_get(request):
    w= Weather.objects.get(id=1)
    return HttpResponse(w.zipcode)

# If method is post create the resources needed for zipcdode under id=1
def zipcode_post(request,zipcode):
    #return HttpResponse("Hello Weather")
    url=weather_url.format(zipcode)

    response = requests.get(url)

    json_response = json.loads(response.text)

    print '---->'
    print json_response
    print '\n'
    #return HttpResponse(json.dumps(json_response))

    w= Weather.objects.get(id=1)
    w.temperature= k_to_f(json_response["main"]["temp"])
    w.zipcode=zipcode
    w.description= json_response["weather"][0]["description"]
    w.save()

    html="<html><body>%s y %s</body></html>"% (w.temperature, w.zipcode) 

    if request.method == 'GET':
        return HttpResponse(html)
    else:
        return HttpResponse("405, Method Not Allowed")

#return the decription in the db
def description(request):
    w= Weather.objects.get(id=1)
    return HttpResponse(w.description)

#return the description of the temp in the db
def temperature(request):
    w= Weather.objects.get(id=1)
    return HttpResponse(w.temperature)
