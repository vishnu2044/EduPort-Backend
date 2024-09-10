from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userprofile.models import (
    UserProfile,
    OtpValidation
    )
from utils import generate_otp
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings


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



class ResendOtpVerification(APIView):
    def post(self, request):
        email = request.data.get('email', '').strip()
        
        # Validate email input
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)


        try:
            user_profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)


        new_otp = generate_otp()


        current_otp, created = OtpValidation.objects.get_or_create(user=user)
        current_otp.otp = new_otp
        current_otp.save()

        # Email context
        context = {
            'user': user,
            'otp': current_otp.otp
        }
        html_message = render_to_string('mail_verify.html', context)
        plain_text = strip_tags(html_message)

        # Send email
        try:
            send_mail(
                subject="Welcome to EduPort. Verify your email.",
                message=plain_text,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                html_message=html_message,
                fail_silently=False
            )
        except Exception as e:
            return Response({"error": "Failed to send OTP via email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Return success response
        return Response(
            {
                "message": "OTP has been sent to your email.",
                "otp": current_otp.otp  # Only include this in development, remove in production
            },
            status=status.HTTP_200_OK
        )
