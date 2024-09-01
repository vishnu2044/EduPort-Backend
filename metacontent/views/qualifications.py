from rest_framework.response import Response
from rest_framework.decorators import APIView
from metacontent.models.qualification import Qualification
from metacontent.serializers.qualifications import QualificationsSerializer


class QulaificatonsListView(APIView):

    def get(self, request):
        qualifications = Qualification.objects.all().order_by('qualification')
        count = qualifications.count()
        serializer = QualificationsSerializer(qualifications, many=True)

        return Response({
            "Message": "States list",
            "total": count,
            "data": serializer.data,
        })
