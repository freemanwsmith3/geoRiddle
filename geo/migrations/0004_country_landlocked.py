# Generated by Django 4.1.7 on 2023-03-06 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0003_country_area_country_borders_country_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='landlocked',
            field=models.BooleanField(default=False),
        ),
    ]