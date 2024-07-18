# Generated by Django 5.0.4 on 2024-05-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0019_remove_policy_category_remove_policyrecord_policy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('coverage_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('term', models.IntegerField(help_text='Term in years')),
            ],
        ),
    ]
