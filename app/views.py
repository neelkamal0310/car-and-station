from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from django.http import HttpResponse
from .models import Station, Vehicle

# Create your views here.


def changeStation(request):
    if not request.GET.get('ids'):
        return HttpResponse('')
    if request.method == 'POST':
        vehicles = request.GET.get('ids', None)
        pks = vehicles.split(',')
        station_id = int(request.POST.get('station'))
        for pk in pks:
            obj = Vehicle.objects.get(pk=pk)
            obj.station = Station.objects.get(pk=station_id)
            obj.save()
        return HttpResponseRedirect('/admin/app/vehicle/')
    stations = Station.objects.all()
    return render(request, 'ind.html', {'stations': stations})
