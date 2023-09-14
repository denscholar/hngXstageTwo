from django.db import models
from django.core.exceptions import ValidationError



# Custom validator to check if a value is a string
def validate_string(value):
    if not isinstance(value, str):
        raise ValidationError("This field must be a string.")

class Person(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True, validators=[validate_string])
    age = models.CharField(max_length=4, null=True, blank=True, validators=[validate_string])
    email =  models.CharField(max_length=254, null=True, blank=True, validators=[validate_string])
    house_address = models.CharField(max_length=250, null=True, blank=True, validators=[validate_string])
    occupation = models.CharField(max_length=50, null=True, blank=True, validators=[validate_string])
    interest = models.CharField(max_length=50, null=True, blank=True, validators=[validate_string])

    def __str__(self):
        return f'{self.name}'
    


