from django.shortcuts import render, redirect

from django.views.generic import DeleteView
from .models import Weather


class WeatherTimeDeleteView(DeleteView):
    model = Weather
    # template_name = 'links/delete_link.html'
    # success_url = '/links/'

def weather_home(request):
    # error = ''
    # if request.method == 'POST':
    #     form = WeatheForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('links_home')
    #     else:
    #         error = 'Undesirable data'
    # form = WeatherForm()
    # cities = Weather.objects.all()
    # data = {
    #     'form': form,
    #     'error': error,
    #     'cities': cities
    # }
    return render(request, 'main/main_basic.html', data)
