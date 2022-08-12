# Generated by Django 4.0.1 on 2022-08-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_remove_user_age_remove_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]