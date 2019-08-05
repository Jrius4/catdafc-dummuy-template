# Generated by Django 2.2.1 on 2019-05-08 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccerplayers', '0004_auto_20190506_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foot', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Leg',
        ),
        migrations.AlterField(
            model_name='soccerplayer',
            name='strongest_foot',
            field=models.ManyToManyField(to='soccerplayers.Foot'),
        ),
    ]
