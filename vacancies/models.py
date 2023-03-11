from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=240)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now_add=True)


class Companies(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
