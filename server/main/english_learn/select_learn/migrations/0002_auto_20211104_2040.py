# Generated by Django 3.0.8 on 2021-11-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userword',
            name='strength',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='userword',
            name='trials',
            field=models.IntegerField(default=0),
        ),
    ]
