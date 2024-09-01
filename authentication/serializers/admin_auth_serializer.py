from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AdminLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Custom claims
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        if not self.user.is_superuser:
            raise ValidationError({'message': 'Only admin can access this page'})

        data['is_admin'] = self.user.is_superuser
        data['status'] = 200
        data['message'] = 'Login successful'
        return data
