from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from userprofile.serializers.instructor_profile import InstructorProfileCreateSerializer
from userprofile.serializers.instructor_profile_update import InstructorProfileUpdateSerialzer, InstructorProfileProfessionalUpdate
from userprofile.serializers.instructor_profile import InstructorProfileSerializer
from userprofile.models import (
    UserProfile,
    ProfessionalDetailsSection
)
from userprofile.models.instructor_profile import InstructorProfile
from django.contrib.auth.models import User


class InstructorProfileView(APIView):
    """
    API view for Instructor profile create.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        user = request.user
        serializer = InstructorProfileCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InstructorProfileDetails(APIView):
    """
    API view to get the Instructor profile.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        print("current user :::", user)
        try:
            data = InstructorProfile.objects.get(user_profile__user=user)
            print("Instructor profile ::: ",data)
            serializer = InstructorProfileSerializer(data)
            return Response(serializer.data)
        except InstructorProfile.DoesNotExist:
            return Response({"error": "Profile not found!"}, status=status.HTTP_404_NOT_FOUND)




    
class InstructorProfileUpdate(APIView):
    """
    API view for Instructor profile update.
    """    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def put(self, request):
        user = request.user
        try:
            user_profile = UserProfile.objects.get(user=user)
            serializer = InstructorProfileUpdateSerialzer(user_profile, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({"Message": "Profile updated successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except UserProfile.DoesNotExist:
            return Response({"Error": "UserProfile not found"}, status = status.HTTP_404_NOT_FOUND)
        
    
class InstructorProfessionalDetailUpdate(APIView):
    """
    API view for Instructor profile Professional details update.
    """    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request):
        user = request.user
        try:
            Professional_details = ProfessionalDetailsSection.objects.get(user_profile__user = user )
            serializer = InstructorProfileProfessionalUpdate(Professional_details, data = request.data, context = {"request": request})
            if serializer.is_valid():
                serializer.save()
                return Response({"Message": "Professional details updated successfully"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ProfessionalDetailsSection.DoesNotExist:
            return Response({"Error": "Pofessional details not found"}, status = status.HTTP_404_NOT_FOUND)

