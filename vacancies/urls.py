from django.urls import path

from vacancies.views import index, VacanciesListView, CompaniesDetailView

urlpatterns = [
    path('', index),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('companies/<int:pk>/', CompaniesDetailView.as_view(), name='company'),
    ]
