from django.urls import path

from .views import form_input, search_result

urlpatterns = [
    path('', form_input, name='main'),
]