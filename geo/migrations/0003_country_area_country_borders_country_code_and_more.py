# Generated by Django 4.1.7 on 2023-03-06 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_currency_alter_country_capital_country_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='area',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='borders',
            field=models.ManyToManyField(to='geo.country'),
        ),
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='lat',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='long',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
    ]