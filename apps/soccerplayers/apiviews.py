from apps.soccerplayers.models import SoccerPlayer
from apps.soccerplayers.serializers import SoccerPlayerSerializer
from rest_framework import generics

# Create your views here.
class SoccerPlayerListCreate(generics.ListCreateAPIView):
     queryset = SoccerPlayer.objects.all()
     serializer_class = SoccerPlayerSerializer