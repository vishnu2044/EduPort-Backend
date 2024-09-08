from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import SignUpSerializer, UserLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from userprofile.models import UserProfile



class UserSignUpView(APIView):
    """
    API view for user sign-up.
    """
    
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully", "user_id": user.id, "email": user.email}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer


class VerifyEmail(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        print("User mail:::: ", email)
        print("User otp:::: ", otp)

        try:
            user_profile = UserProfile.objects.get(user__email = email)
            if user_profile.otp:
                saved_otp = user_profile.otp

                if saved_otp == otp:
                    user_profile.user.is_active = True
                    user_profile.user.save()
                    user_profile.otp = None
                    user_profile.save()
                    return Response({
                        "message": "Otp verfied successfully", 
                        "OTP": otp       # For testing need to remove on deployment
                        }, status=status.HTTP_202_ACCEPTED)
                else:
                    return Response({"Error": "Otp not verified"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"Error":"Email verification not initiated"}, status=status.HTTP_404_NOT_FOUND)
        except UserProfile.DoesNotExist:
            return Response({"Error":"User profile does not found"}, status=status.HTTP_404_NOT_FOUND)