from rest_framework_simplejwt.views import TokenObtainPairView
# from authentication.serializers import (
#     AdminLoginSerializer,
# )

from authentication.serializers.admin_auth_serializer import AdminLoginSerializer

class AdminLogin(TokenObtainPairView):
    serializer_class = AdminLoginSerializer