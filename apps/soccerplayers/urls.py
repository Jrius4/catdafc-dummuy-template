from django.urls import path
from apps.soccerplayers import apiviews

urlpatterns = [
    path('api/soccerplayers/', apiviews.SoccerPlayerListCreate.as_view()),
]