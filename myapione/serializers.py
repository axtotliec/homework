from rest_framework import serializers

from .models import Category, Tableone, Tabletwo

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TableoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tableone
        fields = '__all__'

class TabletwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabletwo
        fields = '__all__'





