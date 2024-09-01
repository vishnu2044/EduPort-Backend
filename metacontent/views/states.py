from rest_framework.decorators import APIView
from metacontent.serializers.states import StateSerializer
from metacontent.models.state import State
from rest_framework.response import Response

class StateListView(APIView):

    def get(self, request):

        states = State.objects.all().order_by('country__name')
        count = states.count()
        serializer = StateSerializer(states, many=True)

        return Response({
            "Message": "States list",
            "total": count,
            "data": serializer.data,
        })