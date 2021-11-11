from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import Station, Vehicle

# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['regdno', 'station', 'fuel', 'odometer', 'booked']
    ordering = ['regdno']
    actions = ['mark_vehicles_booked', 'mark_vehicles_unbooked', 'change_station']

    def mark_vehicles_booked(self, request, queryset):
        queryset.update(booked=True)
        print(queryset.values_list('pk', flat=True))

    def mark_vehicles_unbooked(self, request, queryset):
        queryset.update(booked=False)

    def change_station(self, request, queryset):
        selected = queryset.values_list('pk', flat=True)
        ids = ','.join(str(pk) for pk in selected)
        return HttpResponseRedirect(f'/changeStation/?ids={ids}')

class StationAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'vehicles']


admin.site.register(Station, StationAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.disable_action('delete_selected')
