from django.urls import path

from vacancies.views import index, VacanciesListView, CompaniesDetailView, VacanciesDetailView

urlpatterns = [
    path('', index, name='main'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', VacanciesDetailView.as_view(), name='vacancy'),
    path('companies/<int:pk>/', CompaniesDetailView.as_view(), name='company'),
    ]
