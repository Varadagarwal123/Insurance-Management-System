# Generated by Django 5.0.4 on 2024-05-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0002_customerdetail_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
