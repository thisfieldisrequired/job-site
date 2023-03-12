from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from vacancies.models import Vacancy, Company



class MainPageView(TemplateView):
    template_name = 'vacancies/index.html'
#    get_context_data

class VacanciesListView(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancies.html'


class VacanciesDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'


class CompaniesDetailView(DetailView):
    model = Company
    template_name = 'vacancies/company.html'



