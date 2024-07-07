from django.core.management.base import BaseCommand

from parser.models import Experiences, Employments, Schedules


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        experiences = [
            Experiences(id="noExperience", name="Нет опыта"),
            Experiences(id="between1And3", name="От 1 года до 3 лет"),
            Experiences(id="between3And6", name="От 3 до 6 лет"),
            Experiences(id="moreThan6", name="Более 6 лет")
        ]
        employments = [
            Employments(id="full", name="Полная занятость"),
            Employments(id="part", name="Частичная занятость"),
            Employments(id="project", name="Проектная работа"),
            Employments(id="volunteer", name="Волонтерство"),
            Employments(id="probation", name="Стажировка")
        ]
        schedules = [
            Schedules(id="fullDay", name="Полный день", uid="full_day"),
            Schedules(id="shift", name="Сменный график", uid="shift"),
            Schedules(id="flexible", name="Гибкий график", uid="flexible"),
            Schedules(id="remote", name="Удаленная работа", uid="remote"),
            Schedules(id="flyInFlyOut", name="Вахтовый метод", uid="fly_in_fly_out"),
        ]

        Experiences.objects.bulk_create(experiences, ignore_conflicts=True)
        Employments.objects.bulk_create(employments, ignore_conflicts=True)
        Schedules.objects.bulk_create(schedules, ignore_conflicts=True)
