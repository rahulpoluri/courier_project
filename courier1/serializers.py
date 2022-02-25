from rest_framework import serializers
from .models import *

class Package_SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package_Sizes
        fields  = '__all__'

class Package_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Package_Category
        fields  = '__all__'