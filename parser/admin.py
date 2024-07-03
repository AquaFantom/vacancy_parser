from django.contrib import admin
from .models import Vacancies, Experiences, Employments, Schedules


# Register your models here.
class VacanciesAdmin(admin.ModelAdmin):
    pass


class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


class EmploymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uid')
    search_fields = ('id', 'name')


admin.site.register(Vacancies, VacanciesAdmin)
admin.site.register(Experiences, ExperiencesAdmin)
admin.site.register(Employments, EmploymentsAdmin)
admin.site.register(Schedules, SchedulesAdmin)
