# Generated by Django 3.2.7 on 2021-10-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_activeoffer_reservedoffer_terminatedoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminatedoffer',
            name='status',
            field=models.IntegerField(choices=[(0, 'Terminé'), (1, 'Non terminé'), (2, 'Annulé'), (3, 'Non présenté')], default=0),
        ),
    ]
