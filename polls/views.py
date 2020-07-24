from django.http import HttpResponse, HttpResponseRedirect # noqa: 401
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import VendasSerializer
from .models import Vendas
import csv
import datetime
import pandas as pd
import re

def index(request):
    return HttpResponseRedirect('/vendas')

class VendasFilter(filters.FilterSet):

    date_gte = filters.DateFilter(field_name="data", lookup_expr='gte')
    date_lte = filters.DateFilter(field_name="data", lookup_expr='lte')

    class Meta:

        model = Vendas
        fields = '__all__' 

class VendasList(generics.ListAPIView):

    queryset = Vendas.objects.all()
    serializer_class = VendasSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = VendasFilter 

class VendasDetail(generics.RetrieveAPIView):
    queryset = Vendas.objects.all()
    serializer_class = VendasSerializer


def insert(request, id):
    #1 - csv, 2 - xlxs, 3 - txt, 4 - html
    if id==1:
        with open('polls/data/VENDAS_20190519.csv') as f:
            reader = csv.reader(f)
            next(reader, None)
            for row in reader:
                d = datetime.datetime.strptime(row[0], '%d.%m.%Y').date()
                obj, created = Vendas.objects.get_or_create(
                    data = d,
                    escrv = int(row[1].strip()),
                    material = int(row[2].strip()),
                    grp_merc = int(row[3].strip()),
                    qtd_faturad = row[4].strip(),
                    )
                if created:
                    obj.save()
    if id==2:
        df = pd.read_excel('polls/data/VENDAS_20190520_20190522.xlsx')
        for index, row in df.iterrows():
            d = datetime.datetime.strptime(str(row['data']), '%d.%m.%Y').date()
            obj, created = Vendas.objects.get_or_create(
                data = d,
                escrv = int(str(row['escrv']).strip()),
                material = int(str(row['material']).strip()),
                grp_merc = int(str(row['grp.merc.']).strip()),
                qtd_faturad = str(row['qtd.faturd']).strip(),
                )
            if created:
                obj.save()
    if id==3:
        regex = r"(\d{2}.\d{2}.\d{4})\|(\d*)\s*\|(\d*)\s*\|(\d*)\s*\|\s*(\d*)"
        with open('polls/data/VENDAS_20190523.txt', encoding="utf8", errors='ignore') as f:
            for linha in f:
                x = re.search(regex, linha)
                if x:
                    row = linha.split('|')
                    d = datetime.datetime.strptime(row[1], '%d.%m.%Y').date()
                    obj, created = Vendas.objects.get_or_create(
                        data = d,
                        escrv = int(row[2].strip()),
                        material = int(row[3].strip()),
                        grp_merc = int(row[4].strip()),
                        qtd_faturad = row[5].strip(),
                        )
                    if created:
                        obj.save()                    
                    
    if id==4:
        df = pd.read_html('polls/data/VENDAS_20200524_20200525.html')
        df = df[0]
        for index, row in df.iterrows():
            d = datetime.datetime.strptime(str(row['data']), '%d.%m.%Y').date()
            obj, created = Vendas.objects.get_or_create(
                data = d,
                escrv = int(str(row['escrv']).strip()),
                material = int(str(row['material']).strip()),
                grp_merc = int(str(row['grp.merc.']).strip()),
                qtd_faturad = str(row['qtd.faturd']).strip(),
                )
            if created:
                obj.save()
                    
        
    return HttpResponseRedirect('/vendas')