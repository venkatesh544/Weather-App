from django.http import HttpResponse
from django.shortcuts import render
import requests

def home(request):
    return render(request,'index.html')

def findWeather(request):
    apikey ='81b5547e8c709441fca1b268632dc36d'
    Url ="http://api.openweathermap.org/data/2.5/weather?q={city}%20&appid={apikey}&units=metric"
    city = request.GET['city']
    city = city.lower()
    finalUrl = Url.format(city=city,apikey=apikey)

    data =requests.get(finalUrl)
    print(data.status_code)
    if data.status_code == 200:
        jdata = data.json()
        temp = jdata['main']['temp']
        description = jdata['weather'][0]['description']
        icon = jdata['weather'][0]['icon']
        print(description)
        context = {
            'temp': temp,
            'description': description,
            'city': city,
            'icon': icon
        }

        return render(request, 'icon.html', context)
    else:
        return HttpResponse('please enter the valid city')