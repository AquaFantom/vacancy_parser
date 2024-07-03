import requests
import pprint

params = {
    'text': 'Python-разработчик',
    'salary': 100000,
    'experience': 'between1And3',
    'employment': 'full',
    'schedule': 'remote',
    'responses_count_enabled': True
}
response = requests.get('https://api.hh.ru/vacancies/', params=params)
pprint.pprint(response.json())
print(response.json()['found'])

