from django.contrib import admin
from .models import Topic, Organization, Event

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Topic)
admin.site.register(Organization)
admin.site.register(Event, EventAdmin)
# Register your models here.
