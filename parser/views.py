from django.shortcuts import render, redirect
from .models import Vacancies, Employments, Experiences, Schedules
from .forms import VacancyForm
import requests


def form_input(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            user_request = form.cleaned_data
            return search_result(request, user_request)
    else:
        form = VacancyForm()
    return render(request, 'parser/form_input.html', {'form': form, 'scroll_off': True})


def search_result(request, user_request):
    params = {
        'text': user_request.get('name'),
        'salary': user_request.get('salary'),
        'only_with_salary': user_request.get('only_with_salary'),
        'responses_count_enabled': True
    }

    try:
        experience = Experiences.objects.get(name=user_request['experience'])
        params['experience'] = experience.id
    except Experiences.DoesNotExist:
        ...
    try:
        employment = Employments.objects.get(name=user_request['employment'])
        params['employment'] = employment.id
    except Employments.DoesNotExist:
        ...
    try:
        schedule = Schedules.objects.get(name=user_request['schedule'])
        params['schedule'] = schedule.id
    except Schedules.DoesNotExist:
        ...

    response = requests.get('https://api.hh.ru/vacancies', params=params)
    response_json = response.json()
    if response.status_code == 200:
        vacancies = []
        for item in response_json.get('items'):
            salary_size = None
            if salary := item.get('salary'):
                salary_size = salary.get('to')
                if salary_size is None:
                    salary_size = salary.get('from')
            vacancies.append(Vacancies(id=item.get('id'), url=item.get('alternate_url'), name=item.get('name'), salary=salary_size))
        Vacancies.objects.bulk_create(vacancies, ignore_conflicts=True)

        context = {
            'vacancies': response_json.get('items'),
            'found': response_json.get('found')
        }
        return render(request, 'parser/search_result.html', context)
    else:
        context = {
            'found': 0
        }
        return render(request, 'parser/search_result.html', context)

