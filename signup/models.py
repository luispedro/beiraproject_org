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
    email = models.EmailField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.now)
    nr_guests = models.PositiveIntegerField(default=1, verbose_name='Including myself, I will bring these many people')
    attribution = models.CharField(max_length=2, choices=_Attribution_Choices, default='ME')
    attribute_to = models.CharField(max_length=255, default='Myself')
    donation = models.IntegerField(default=35, help_text="Recommended: $35 per person")
    join_ml = models.BooleanField(verbose_name='Join Our Mailing List')
    attend = models.BooleanField(verbose_name='I am attending on the 3rd', default=True)

    def __unicode__(self):
        return self.name

class SignupForm(ModelForm):
    class Meta:
        model = Signup
        exclude = ('date',)
