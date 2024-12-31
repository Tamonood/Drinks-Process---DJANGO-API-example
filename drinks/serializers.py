#defines the process of GOING FROM A PYTHON OBJECT TO JSON

from rest_framework import serializers
from .models import Drink

#inherit from model 
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']


    
    '''
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name + "-" + self.description
    '''