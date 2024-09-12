from django.db import models


class MyModel(models.Model):
    # CharField for short text
    name = models.CharField(max_length=100)
    
    # TextField for long text
    description = models.TextField()
    
    # IntegerField for whole numbers
    age = models.IntegerField()
    
    # DateField for dates
    birth_date = models.DateField()
    
    # EmailField for email addresses
    email = models.EmailField()
    
    # BooleanField for True/False values
    is_active = models.BooleanField(default=True)
    
    # ForeignKey for many-to-one relationships
    related_model = models.ForeignKey('AnotherModel', on_delete=models.CASCADE)

class AnotherModel(models.Model):
    title = models.CharField(max_length=100)
