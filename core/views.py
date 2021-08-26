import json
import urllib.request

from django.shortcuts import render


def index(request):
    if request.method == "POST":
        city = request.POST["city"]
        res = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid=b01642279ed58a8c75bd925993afc12b"
        ).read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data["sys"]["country"]),
            "coordinate": str(json_data["coord"]["lon"]) + " " + str(json_data["coord"]["lat"]),
            "temprature": int(json_data["main"]["temp"]) - 273.15,
            "pressure": str(json_data["main"]["pressure"]),
            "humidity": str(json_data["main"]["humidity"]) + "%",
        }

    else:
        city = ""
        data = {}
    return render(request, "index.html", {"city": city, "data": data})
