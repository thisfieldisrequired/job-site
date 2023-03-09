from django.urls import path

from vacancies.views import index


urlpatterns = [
    path('', index),
]
