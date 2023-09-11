from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email =  models.EmailField(max_length=254, null=True, blank=True)
    house_address = models.CharField(max_length=250, null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


