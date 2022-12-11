from rest_framework import serializers
from .models import Demography, Chart

class DemographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Demography # this is the model that is being serialized
        fields = ('id', 'dbn', 'school_name', 'category', 'total_enrollment')

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart 
        fields = ('id', 'created_date')