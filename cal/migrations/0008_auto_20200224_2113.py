# Generated by Django 3.0.3 on 2020-02-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0007_auto_20200224_2039'),
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
            field=models.TimeField(blank=True, null=True),
        ),
    ]
