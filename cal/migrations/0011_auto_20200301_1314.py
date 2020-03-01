# Generated by Django 3.0.3 on 2020-03-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0010_auto_20200228_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='fact_close_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='days',
            name='fact_open_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='grade',
            field=models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_names',
            field=models.CharField(choices=[('samosa', 'SAMOSA'), ('gota', 'GOTA'), ('chana dal', 'CHANA DAL'), ('sing bhujiya', 'SING BHUJIYA'), ('bhakharwadi', 'BHAKHARWADI'), ('chakari', 'CHAKARI'), ('soya stick', 'SOYA STICK'), ('fulwadi', 'FULWADI'), ('kala jam', 'KALA JAM'), ('gulab jamun', 'GULAB JAMUN'), ('mohanthal(pure ghee)', 'MOHANTHAL(PURE GHEE)'), ('magadal(pure ghee)', 'MAGADAL(PURE GHEE)'), ('namkeen', 'NAMKEEN'), ('tikha-mitha', 'TIKHA-MITHA'), ('khatta-mitha', 'KHATTA-MITHA'), ('poha chewdo', 'POHA CHEWDO'), ('farali chewdo', 'FARALI CHEWDO'), ('bhavnagari ganthiya', 'BHAVNAGARI GANTHIYA'), ('chakari ganthiya', 'CHAKARAI GANTHIYA'), ('mari ganthiya', 'MARI GANTHIYA'), ('bhel', 'BHEL'), ('gajar halwo', 'GAJAR HALWO'), ('farsipuri', 'FARSIPURI'), ('sakkarpara', 'SAKKARPARA'), ('mohanthal', 'MOHANTHAL'), ('ladu', 'LADU'), ('magadal', 'MAGALDAL'), ('mesur', 'MESUR'), ('devda', 'DEVDA'), ('bundi', 'BUNDI'), ('barfi', 'BARFI'), ('peda(shekela)', 'PEDA(SHEKELA)'), ('peda(kesar)', 'PEDA(KESAR)'), ('peda(white)', 'PEDA(WHITE)'), ('dudh halwo', 'DUDH HALWO'), ('dudhi halwo', 'DUDHI HALWO'), ('shrikhand', 'SHRIKHAND'), ('lassi', 'LASSI'), ('chhash', 'CHHASH')], max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='worker',
            field=models.CharField(choices=[('satish kumar', 'SATISH KUMAR'), ('rona ji', 'RONA JI'), ('ishwar lal', 'ISHWAR LAL'), ('babu', 'BABU'), ('sanjay', 'SANJAY')], max_length=50),
        ),
    ]
