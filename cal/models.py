from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from django.forms import TextInput, Textarea
from django import forms
from django.conf import settings

# worker_names = (

#     ('satish kumar', 'SATISH KUMAR'),
#     ('rona ji','RONA JI'),
#     ('ishwar lal','ISHWAR LAL'),
#     ('babu','BABU'),
#     ('sanjay','SANJAY'),
# )




# item_names = (
    
#    ('samosa', 'SAMOSA'),('gota', 'GOTA'),('chana dal','CHANA DAL'),('sing bhujiya', 'SING BHUJIYA'),('bhakharwadi', 'BHAKHARWADI'), ('chakari', 'CHAKARI'), ('soya stick', 'SOYA STICK'), ('fulwadi', 'FULWADI'), ('kala jam', 'KALA JAM'), ('gulab jamun', 'GULAB JAMUN'), ('mohanthal(pure ghee)', 'MOHANTHAL(PURE GHEE)'), ('magadal(pure ghee)', 'MAGADAL(PURE GHEE)'),
#    ('namkeen', 'NAMKEEN'), ('tikha-mitha', 'TIKHA-MITHA'), ('khatta-mitha', 'KHATTA-MITHA'), ('poha chewdo', 'POHA CHEWDO'), ('farali chewdo', 'FARALI CHEWDO'),( 'bhavnagari ganthiya',  'BHAVNAGARI GANTHIYA'), ('chakari ganthiya', 'CHAKARAI GANTHIYA'), ('mari ganthiya', 'MARI GANTHIYA'), ('bhel', 'BHEL'),('gajar halwo', 'GAJAR HALWO') , 
#    ('farsipuri', 'FARSIPURI'),('sakkarpara', 'SAKKARPARA'),('mohanthal', 'MOHANTHAL') , ('ladu', 'LADU'), ('magadal', 'MAGALDAL'), ('mesur', 'MESUR'),('devda', 'DEVDA') , ('bundi','BUNDI'),('barfi', 'BARFI') , ('peda(shekela)', 'PEDA(SHEKELA)'), ('peda(kesar)', 'PEDA(KESAR)'), ( 'peda(white)', 'PEDA(WHITE)'), ('dudh halwo', 'DUDH HALWO'),( 'dudhi halwo', 'DUDHI HALWO'), 
#    ('shrikhand', 'SHRIKHAND'), ('lassi', 'LASSI'), ('chhash', 'CHHASH'),

# )

grades = (

    ('a', 'A'), ('b','B'), ('c', 'C'), ('d', 'D')
)

class item(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True, default='0')    
    name = models.CharField(max_length=100)
    offset = models.FloatField(default="0.0")
    created_date = models.DateField(default = date.today)
    updated_date = models.DateField(default = date.today, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return str(self.name)

class worker(models.Model):
    worker_id = models.PositiveIntegerField(primary_key=True, default='0')    
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return str(self.name)

class item_preparation_detail(models.Model):
    rweight = models.FloatField(default="0.0")
    note = models.TextField(max_length=1000, blank=True, null=True)    
    grade = models.CharField(max_length=1, choices=grades)
    date = models.DateField(default = date.today)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    item_id = models.ForeignKey(item, on_delete=models.PROTECT, null=True)
    worker_id = models.ForeignKey(worker, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return str(self.pk)

class note(models.Model):
    note_id = models.AutoField(primary_key=True)   
    setup = models.TextField(max_length=1000, blank=True, null=True)
    cleansing = models.TextField(max_length=1000, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    def __str__(self):
        return str(self.pk)


class factorylog(models.Model):
    factorylog_id = models.AutoField(primary_key=True)
    date = models.DateField(default = date.today, unique=True)
    fact_open_time = models.TimeField(default="10:00 AM")
    fact_close_time = models.TimeField(default="10:00 PM", blank=True, null=True)
    note_id = models.ForeignKey(note, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.pk)