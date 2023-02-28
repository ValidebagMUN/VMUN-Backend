from django.contrib import admin

from .models import Committee, Conference, Institution


class ConferenceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "venue", "host", "start", "end")
    list_filter = ("name", "slug", "venue", "host", "start", "end")
    search_fields = ("name", "slug", "venue", "host", "start", "end")


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "conference")
    list_filter = ("name", "slug", "conference")
    search_fields = ("name", "slug", "conference")


class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "address")
    list_filter = ("name", "slug", "address")
    search_fields = ("name", "slug", "address")


admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Institution, InstitutionAdmin)
