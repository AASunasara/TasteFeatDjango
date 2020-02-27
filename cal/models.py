from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


worker_names = (

    ('satish kumar', 'SATISH KUMAR'),
    ('ronaji','RONAJI'),
    ('ishwar lal','ISHWAR LAL'),
    ('babu','BABU'),
    ('sanjay','SANJAY'),
)




item_names = (
    
   ('samosa', 'SAMOSA'),('gota', 'GOTA'),('chana dal','CHANA DAL'),('sing bhujiya', 'SING BHUJIYA'),('bhakharwadi', 'BHAKHARWADI'), ('chakari', 'CHAKARI'), ('soya stick', 'SOYA STICK'), ('fulwadi', 'FULWADI'), ('kala jam', 'KALA JAM'), ('gulab jamun', 'GULAB JAMUN'), ('mohanthal(pure ghee)', 'MOHANTHAL(PURE GHEE)'), ('magadal(pure ghee)', 'MAGADAL(PURE GHEE)'),
   ('namkeen', 'NAMKEEN'), ('tikha-mitha', 'TIKHA-MITHA'), ('khatta-mitha', 'KHATTA-MITHA'), ('poha chewdo', 'POHA CHEWDO'), ('farali chewdo', 'FARALI CHEWDO'),( 'bhavnagari ganthiya',  'BHAVNAGARI GANTHIYA'), ('chakari ganthiya', 'CHAKARAI GANTHIYA'), ('mari ganthiya', 'MARI GANTHIYA'), ('bhel', 'BHEL'),('gajar halwo', 'GAJAR HALWO') , 
   ('farsipuri', 'FARSIPURI'),('sakkarpara', 'SAKKARPARA'),('mohanthal', 'MOHANTHAL') , ('ladu', 'LADU'), ('magadal', 'MAGALDAL'), ('mesur', 'MESUR'),('devda', 'DEVDA') , ('bundi','BUNDI'),('barfi', 'BARFI') , ('peda(shekela)', 'PEDA(SHEKELA)'), ('peda(kesar)', 'PEDA(KESAR)'), ( 'peda(white)', 'PEDA(WHITE)'), ('dudh halwo', 'DUDH HALWO'),( 'dudhi halwo', 'DUDHI HALWO'), 
   ('shrikhand', 'SHRIKHAND'), ('lassi', 'LASSI'), ('chhash', 'CHHASH'),

)

grades = (

    ('a', 'A'), ('b','B'), ('c', 'C'), ('d', 'D')
)

class items(models.Model):
    item_names = models.CharField(max_length=50, choices=item_names, default="SAMOSA")
    rweight = models.IntegerField(default=0.0)
    iweight = models.IntegerField(default=0.0)
    grade = models.CharField(max_length=1, choices=grades, default="A")
    worker = models.CharField(max_length=50, choices=worker_names, default="SATISH KUMAR")
    note = models.CharField(max_length=200, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(default = date.today)

    def __str__(self):
        return str(self.pk)

class days(models.Model):
    date = models.DateField(default = date.today, unique=True)
    fact_open_time = models.TimeField(blank=True, null=True)
    fact_close_time = models.TimeField(blank=True, null=True)
    setup = models.CharField(max_length=20, blank=True)
    cleansing = models.CharField(max_length=20, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pk)
