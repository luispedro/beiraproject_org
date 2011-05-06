from django.db import models
from django.forms import ModelForm
from datetime import datetime

_Attribution_Choices = (
    ('ME', 'To myself'),
    ('SO', 'To the person below'),
    ('NO', 'Anynomous')
    )

class Signup(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField(default=datetime.now)
    nr_guests = models.PositiveIntegerField()
    attribution = models.CharField(max_length=2, choices=_Attribution_Choices)
    donation = models.IntegerField(default=35)
    join_ml = models.BooleanField()
    attend = models.BooleanField()

    def __unicode__(self):
        return self.name

class SignupForm(ModelForm):
    class Meta:
        model = Signup

