from django.contrib import admin
from .models import CatdaSoccerPlayer, CatdaExecutiveTeam, CatdaFoot,CatdaTeamPosition,CatdaTechnicalTeam


admin.site.register(CatdaSoccerPlayer)
admin.site.register(CatdaExecutiveTeam)
admin.site.register(CatdaFoot)
admin.site.register(CatdaTeamPosition)
admin.site.register(CatdaTechnicalTeam)

# Register your models here.
