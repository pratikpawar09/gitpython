from django.db import models

# Create your models here.

class Sample(models.Model):
    name = models.CharField('name',max_length=20)
    salary = models.FloatField('salary')
    age = models.IntegerField('age')
    desig= models.CharField('designation', max_length=20)


class Emp(models.Model):
    name = models.CharField('name',max_length=20)
    salary = models.FloatField('salary')
    age = models.IntegerField('age')
    desig= models.CharField('designation', max_length=20)
