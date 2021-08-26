from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100 ,default='DEFAULT VALUE')
    details =  models.CharField(max_length=500, default='DEFAULT VALUE')

class Tours:
    content: str
    day: str
    details: str
    button: str

class ticket:
    month : str
    numb: int
    stat: str

class img:
    name: str