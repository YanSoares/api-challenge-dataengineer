import datetime

from django.db import models
from django.utils import timezone

class Vendas(models.Model):

    class Meta:

        db_table = 'vendas'

    data = models.DateField()
    escrv = models.IntegerField()
    material = models.IntegerField()
    grp_merc = models.IntegerField()
    qtd_faturad = models.CharField(max_length=5)
