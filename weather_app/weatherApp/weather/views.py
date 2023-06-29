from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    url = "http://api.weatherapi.com/v1/forecast.json?q={}&key=c991cbdb98134f1781b231518232006"
    form = CityForm

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()


    cities = City.objects.all()
    cities_data = []
    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_data = {
            'id':int(city.id),
        'city_name' : r['location']['name'],
        'country' : r['location']['country'],
        'temp': r['current']['temp_c'],
        'icon':r['current']['condition']['icon'],
        'description':r['current']['condition']['text']
        }
        cities_data.append(city_data)
        
    return render(request, 'index.html',{'cities_data':cities_data, 'form':form})

class CityDeleteView(DeleteView):
    model = City
    template_name = "delete_city.html"
    success_url= reverse_lazy('home')
