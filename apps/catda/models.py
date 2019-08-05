from django.db import models
from apps.posts.models import Author
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class CatdaTeamPosition(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class CatdaFoot(models.Model):
    foot = models.CharField(max_length=30)

    def __str__(self):
        return self.foot


class CatdaSoccerPlayer(models.Model):
    full_name = models.CharField(max_length=100)
    short_description = models.TextField()
    bio = RichTextUploadingField(blank=True, null=True)
    catda_team_positions = models.ManyToManyField(CatdaTeamPosition)
    catda_strongest_foot = models.ManyToManyField(CatdaFoot)
    ratings = models.IntegerField(default=0,null=True)
    team_number = models.IntegerField(default=1,null=True)
    dob = models.CharField(max_length=100)
    former_team = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bio_picture = models.ImageField()
    featured_picture = models.ImageField()
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


    def get_absolute_url(self):
        return reverse('player-detail', kwargs={
            'id':self.pk
        })


class CatdaTechnicalTeam(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    bio = RichTextUploadingField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bio_picture = models.ImageField()
    featured_picture = models.ImageField()
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('technical-member-detail', kwargs={
            'id':self.pk
        })



class CatdaExecutiveTeam(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    bio = RichTextUploadingField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bio_picture = models.ImageField()
    featured_picture = models.ImageField()
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('executive-detail', kwargs={
            'id':self.pk
        })
