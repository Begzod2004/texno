
from rest_framework import serializers
from technique.models import *


class techniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = technique
        fields = '__all__'



class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'



class sizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = size
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        
