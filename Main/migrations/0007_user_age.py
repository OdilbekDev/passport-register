# Generated by Django 4.0.1 on 2022-08-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_remove_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
