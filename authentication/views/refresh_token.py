
from rest_framework_simplejwt.views import TokenViewBase

from authentication.serializers.token_refresh_serializer import TokenRefreshSerializer



class TokenRefresh(TokenViewBase):
    serializer_class = TokenRefreshSerializer
