from django.shortcuts import render
from django.views.generic import ListView, DetailView
from vacancies.models import Vacancy, Company


def index(request):
    return render(request, 'vacancies/index.html')


class VacanciesListView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'


class VacanciesDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'


class CompaniesDetailView(DetailView):
    model = Company
    template_name = 'vacancies/company.html'


