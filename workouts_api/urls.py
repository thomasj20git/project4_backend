from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkoutList.as_view(), name='workout_list'), # api/contacts will be routed to the ContactList view for handling
    path('<int:pk>', views.WorkoutDetail.as_view(), name='workout_detail'), # api/contacts will be routed to the ContactDetail view for handling
]