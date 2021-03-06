# Generated by Django 3.0.8 on 2021-11-04 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSentence',
            fields=[
                ('sentence_id', models.AutoField(db_column='sentence_id', default=0, primary_key=True, serialize=False, unique=True)),
                ('sentence_text', models.TextField()),
                ('sentence_user', models.ForeignKey(db_column='sentence_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserWord',
            fields=[
                ('word_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('word', models.TextField()),
                ('strength', models.FloatField()),
                ('trials', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sentence_id', models.ForeignKey(db_column='sentence_id', default=0, on_delete=django.db.models.deletion.CASCADE, to='select_learn.UserSentence')),
                ('user_id', models.ForeignKey(db_column='user_id', default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('word_id', 'user_id')},
            },
        ),
    ]
