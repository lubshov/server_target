from django.contrib import admin
from .models import ListeningResponses


class ListeningResponsesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('text',)
    search_fields = ('text',)


admin.site.register(ListeningResponses, ListeningResponsesAdmin)
