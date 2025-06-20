from django.contrib import admin
from .models import Device, Payload


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['devEUI', 'latest_status', 'created_at', 'updated_at']
    list_filter = ['latest_status', 'created_at']
    search_fields = ['devEUI']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Payload)
class PayloadAdmin(admin.ModelAdmin):
    list_display = ['device', 'fCnt', 'status', 'decoded_data', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['device__devEUI']
    readonly_fields = ['created_at']
    raw_id_fields = ['device']