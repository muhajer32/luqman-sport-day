from django.contrib import admin

from .models import Activity, Participant

class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 1

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age_group', 'gender')
    search_fields = ('first_name', 'last_name', 'age_group', 'gender')

admin.site.register(Activity)
