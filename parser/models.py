from django.db import models


class Vacancies(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID вакансии')
    url = models.URLField(max_length=200, verbose_name='Ссылка на вакансию')
    name = models.CharField(max_length=500, verbose_name='Название вакансии')
    salary = models.IntegerField(null=True, blank=True, verbose_name='Размер заработной платы', default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Experiences(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, verbose_name='Опыт работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыты работы'


class Employments(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, verbose_name='Тип занятости')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип занятости'
        verbose_name_plural = 'Типы занятости'


class Schedules(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, verbose_name='График работы')
    uid = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Графики работы'
