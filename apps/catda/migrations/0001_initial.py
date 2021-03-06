# Generated by Django 2.1.11 on 2019-08-13 09:47

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatdaExecutiveTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bio_picture', models.ImageField(upload_to='')),
                ('featured_picture', models.ImageField(upload_to='')),
                ('featured', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
            ],
        ),
        migrations.CreateModel(
            name='CatdaFoot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foot', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CatdaSoccerPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ratings', models.IntegerField(default=0, null=True)),
                ('team_number', models.IntegerField(default=1, null=True)),
                ('dob', models.CharField(max_length=100)),
                ('former_team', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bio_picture', models.ImageField(upload_to='')),
                ('featured_picture', models.ImageField(upload_to='')),
                ('featured', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
                ('catda_strongest_foot', models.ManyToManyField(to='catda.CatdaFoot')),
            ],
        ),
        migrations.CreateModel(
            name='CatdaTeamPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CatdaTechnicalTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bio_picture', models.ImageField(upload_to='')),
                ('featured_picture', models.ImageField(upload_to='')),
                ('featured', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Author')),
            ],
        ),
        migrations.AddField(
            model_name='catdasoccerplayer',
            name='catda_team_positions',
            field=models.ManyToManyField(to='catda.CatdaTeamPosition'),
        ),
    ]
