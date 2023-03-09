from django.urls import path

from vacancies.views import index, VacanciesListView

urlpatterns = [
    path('', index),
    path('vacancies/', VacanciesListView.as_view())
    ]
