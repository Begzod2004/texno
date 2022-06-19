
from rest_framework import serializers
from home.models import *


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = '__all__'



class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'



class FpsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fps
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

