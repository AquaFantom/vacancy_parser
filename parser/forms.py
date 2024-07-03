from django import forms

from .models import Experiences, Employments, Schedules


class VacancyForm(forms.Form):
    name = forms.CharField(label='Название вакансии', max_length=200, widget=forms.TextInput(attrs={'class': 'form'
                                                                                                             '-control'}))
    salary = forms.IntegerField(label='Размер заработной платы (в RUB)', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    experience = forms.ModelChoiceField(label='Опыт работы', widget=forms.Select(attrs={'class': 'form-control'}), queryset=Experiences.objects.all(), required=False)
    employment = forms.ModelChoiceField(label='Тип занятости', widget=forms.Select(attrs={'class': 'form-control'}), queryset=Employments.objects.all(), required=False)
    schedule = forms.ModelChoiceField(label='График работы', widget=forms.Select(attrs={'class': 'form-control'}), queryset=Schedules.objects.all(), required=False)
    only_with_salary = forms.BooleanField(label='Искать только вакансии с указанием зарплаты', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
