from rest_framework.views import APIView
from rest_framework.response import Response
from .routes import API_ROUTES


class GetRoutes(APIView):
    def get(self, request):
        return Response(API_ROUTES)