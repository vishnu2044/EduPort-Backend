from rest_framework.views import APIView
from rest_framework.response import Response
from metacontent.serializers.countries import CountriesSerializer
from metacontent.models.country import Country

class CountriesListView(APIView):
    def get(self, request):
        countries = Country.objects.all().order_by('name')
        count = countries.count()
        serializer = CountriesSerializer(countries, many=True)

        return Response({
            "Message": "Countries list",
            "total": count,
            "data": serializer.data,
        })
