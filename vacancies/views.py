from django.shortcuts import render
from django.views.generic import ListView, DetailView
from vacancies.models import Vacancies, Companies


def index(request):
    return render(request, 'vacancies/index.html')


class VacanciesListView(ListView):
    model = Vacancies
    template_name = 'vacancies/vacancies.html'


class VacanciesDetailView(DetailView):
    model = Vacancies
    template_name = 'vacancies/vacancy.html'


class CompaniesDetailView(DetailView):
    model = Vacancies
    template_name = 'vacancies/company.html'

