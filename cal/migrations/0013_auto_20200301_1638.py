# Generated by Django 3.0.3 on 2020-03-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0012_auto_20200301_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='cleansing',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='days',
            name='setup',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
