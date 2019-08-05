from rest_framework import serializers
from apps.soccerplayers.models import SoccerPlayer

class SoccerPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerPlayer
        #fields = ('id', 'name', 'email', 'message')
        fields = ('__all__')