# Generated by Django 5.0.4 on 2024-05-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0004_ajents_age_ajents_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ajents',
            name='Phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ajents',
            name='end_Time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ajents',
            name='start_Time',
            field=models.IntegerField(null=True),
        ),
    ]
