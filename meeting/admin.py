from django.contrib import admin
from models import MeetingRoom, OutuptServer, Meeting


# Register your models here.

@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'channel_name', 'ice_host', 'ice_port', 'ice_mount']
    fields = ['title', 'channel_name', 'ice_host', 'ice_port', 'ice_mount']


@admin.register(OutuptServer)
class OutputServerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'mroom', 'url']


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'mroom', 'title']
