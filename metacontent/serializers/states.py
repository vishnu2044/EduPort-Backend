from rest_framework import serializers
from metacontent.models.state import State
from metacontent.serializers.countries import CountriesSerializer

class StateSerializer(serializers.ModelSerializer):
    country = CountriesSerializer()

    class Meta:
        model = State

        fields = (
            'id',
            'name',
            'country'

        )
    
    # def get_country_name(self, obj):
    #     return obj.country.name