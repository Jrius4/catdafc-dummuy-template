from django import forms
from .models import CatdaSoccerPlayer, CatdaExecutiveTeam, CatdaTeamPosition,CatdaTechnicalTeam
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CatdaSoccerPlayersForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget(
        attrs={'required': False, 'col': 30, 'rows': 10}
    ))


    class Meta:
        model = CatdaSoccerPlayer
        fields = ('full_name','short_description','bio','catda_team_positions','catda_strongest_foot','ratings','team_number','dob','former_team','bio_picture','author','featured_picture','featured',)


class CatdaExecutiveForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget(
        attrs={'required': False, 'col': 30, 'rows': 10}
    ))

    class Meta:
        model = CatdaExecutiveTeam
        fields = ('full_name','title','short_description','author','bio','bio_picture','featured_picture','featured')


class CatdaTechnicalMemberForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorUploadingWidget(
        attrs={'required': False, 'col': 30, 'rows': 10}
    ))
    class Meta:
        model = CatdaTechnicalTeam
        fields = ('full_name','title','short_description','bio','author','bio_picture','featured_picture','featured')




# class ExecutivesForm(forms.ModelForm):
#     class Meta:


# class TechnicalTeamForm(forms.ModelForm):
#     class Meta:


# class StoreForm(forms.ModelForm):
#     class Meta:
#         pass