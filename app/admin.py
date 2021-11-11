from django.contrib import admin
from .models import Station, Vehicle

# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['regdno', 'station', 'fuel', 'odometer', 'booked']
    ordering = ['regdno']
    actions = ['mark_vehicles_booked', 'mark_vehicles_unbooked']

    def mark_vehicles_booked(self, request, queryset):
        queryset.update(booked=True)

    def mark_vehicles_unbooked(self, request, queryset):
        queryset.update(booked=False)


class StationAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'vehicles']


admin.site.register(Station, StationAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.disable_action('delete_selected')
