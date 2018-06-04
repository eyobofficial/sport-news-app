from django.contrib import admin
from . import models


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'team_type', 'country', ]
    list_filter = ['country', 'team_type', ]
    prepopulated_fields = {'slug': ('translation', )}


@admin.register(models.Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ['name', 'competition_type', 'is_featured', ]
    list_filter = ['is_featured', 'competition_type', ]
    prepopulated_fields = {'slug': ('translation', )}


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'first_team', 'second_team',
        'match_status', 'is_featured',
    ]
    list_filter = ['is_featured', 'competition', ]
    prepopulated_fields = {'slug': ('translation', )}

