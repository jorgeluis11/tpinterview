from django.contrib import admin

from .models import Language


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language')
    list_display_links = ['id', 'language']
    # list_filter = ['rating', 'status']
    search_fields = ['id', 'language']

admin.site.register(Language, LanguageAdmin)
