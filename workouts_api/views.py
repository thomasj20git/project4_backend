from rest_framework import generics
from .serializers import WorkoutSerializer
from .models import Workout

class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = WorkoutSerializer # tell django what serializer to use

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all().order_by('id')
    serializer_class = WorkoutSerializer