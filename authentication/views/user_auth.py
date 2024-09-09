from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import SignUpSerializer, UserLoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from userprofile.models import (
    UserProfile,
    OtpValidation
    )




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

        try:
            user_profile = UserProfile.objects.get(user__email = email)
            try:
                otp_check = OtpValidation.objects.get(user__email = email)
            except OtpValidation.DoesNotExist:
                return Response({"error":"User profile does not found"}, status=status.HTTP_404_NOT_FOUND)
            if otp_check.otp:
                if otp_check.is_otp_valid():
                        
                    saved_otp = otp_check.otp

                    if saved_otp == otp:
                        user_profile.user.is_active = True
                        user_profile.user.save()

                        return Response({
                            "message": "Otp verfied successfully", 
                            }, status=status.HTTP_202_ACCEPTED)
                    else:
                        return Response({"error": "Otp not verified"}, status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response({"error": "OTP has expired"})
            else:
                return Response({"error":"Email verification not initiated"}, status=status.HTTP_404_NOT_FOUND)
        
        except UserProfile.DoesNotExist:
            return Response({"error":"User profile does not found"}, status=status.HTTP_404_NOT_FOUND)
        
