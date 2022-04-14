from rest_framework import serializers 
from .models import Workout
class WorkoutSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Workout # tell django which model to use
        fields = ('id', 'date', 'excercises', 'notes') # tell django which fields to include