# Generated by Django 4.1.1 on 2022-10-06 18:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='user_group',
            field=models.ManyToManyField(related_name='api_userdata_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
