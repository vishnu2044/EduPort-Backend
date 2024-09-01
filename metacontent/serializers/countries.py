from rest_framework import serializers
from metacontent.models.country import Country

class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = (
            'id',
            'name'
        )