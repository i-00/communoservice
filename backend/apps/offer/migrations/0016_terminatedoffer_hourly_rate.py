# Generated by Django 3.2.7 on 2021-12-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0015_reservedoffer_hourly_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminatedoffer',
            name='hourly_rate',
            field=models.DecimalField(decimal_places=2, default='13.50', max_digits=6),
        ),
    ]
