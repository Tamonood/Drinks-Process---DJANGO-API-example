from django.db import models

class Drink(models.Model): #inherit from model class
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    def __str__(self):
        #return self.name + "-" + self.description
        return self.name + "-" + self.description