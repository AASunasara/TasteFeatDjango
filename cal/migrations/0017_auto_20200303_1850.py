# Generated by Django 3.0.3 on 2020-03-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0016_auto_20200302_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='note',
            field=models.TextField(),
        ),
    ]