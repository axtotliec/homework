from rest_framework import serializers

from .models import Category, Tableone, Tabletwo, Tablethree

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

class TablethreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablethree
        fields = '__all__'





