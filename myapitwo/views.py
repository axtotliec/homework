from django.shortcuts import render

#Filtro
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# views.py Add Axtotliec
from rest_framework import viewsets

from .serializers import CategorySerializer, TableoneSerializer, TabletwoSerializer, TablethreeSerializer
from .models import Category, Tableone, Tabletwo, Tablethree

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-pk')
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('active',)
    search_fields = ('title',)

class TableoneViewSet(viewsets.ModelViewSet):
    queryset = Tableone.objects.all().order_by('-pk')
    serializer_class = TableoneSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id_cate', 'active')
    search_fields = ('title', 'tipe')

class TabletwoViewSet(viewsets.ModelViewSet):
    queryset = Tabletwo.objects.all().order_by('-pk')
    serializer_class = TabletwoSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id_cate', 'active')
    search_fields = ('title', 'tipe')

class TablethreeViewSet(viewsets.ModelViewSet):
    queryset = Tablethree.objects.all().order_by('-pk')
    serializer_class = TablethreeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id_cate', 'active')
    search_fields = ('title', 'tipe')


    