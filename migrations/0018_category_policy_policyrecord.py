# Generated by Django 5.0.4 on 2024-05-29 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0017_customerdetail_address_customerdetail_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('creation_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=200)),
                ('sum_assurance', models.PositiveIntegerField()),
                ('premium', models.PositiveIntegerField()),
                ('tenure', models.PositiveIntegerField()),
                ('creation_date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insurance.category')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('creation_date', models.DateField(auto_now=True)),
                ('Policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insurance.policy')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Insurance.customerdetail')),
            ],
        ),
    ]
