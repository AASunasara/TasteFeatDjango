# Generated by Django 3.0.3 on 2020-03-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0011_auto_20200301_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='fact_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='days',
            name='fact_open_time',
            field=models.TimeField(),
        ),
    ]
