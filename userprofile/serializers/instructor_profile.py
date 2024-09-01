from rest_framework import serializers
from django.core.exceptions import ValidationError
from userprofile.models.user_profile import UserProfile
from userprofile.models.instructor_profile import InstructorProfile
from userprofile.models.professional_details import ProfessionalDetailsSection
from metacontent.models.qualification import Qualification
from metacontent.models.country import Country
from metacontent.models.state import State
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',  # If 'is_admin' is a custom field, use it. Otherwise, Django uses 'is_staff'.
            'is_active',
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'phone',
            'alternate_email',
            'alternate_phone',
            'date_of_birth',
            'gender',
            'created_at',
            'updated_at',
        ]

class UserProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalDetailsSection
        fields = [
            'id',
            'occupation',
            'area_job_place',
            'experience',
            'qualification',
            'state_job_place',
            'country_job_place',
            'created_at',
        ]

class InstructorProfileSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    professional_details = UserProfessionalSerializer()

    class Meta:
        model = InstructorProfile
        fields = [
            'id',
            'user_profile',
            'professional_details',
        ]



class InstructorProfileCreateSerializer(serializers.ModelSerializer):
    # User model fields
    phone = serializers.CharField(max_length=15, required=False, allow_null=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    gender = serializers.CharField(max_length=15, required=False, allow_null=True)

    # Professional details model fields
    occupation = serializers.CharField(max_length=255, allow_null=True)
    area_job_place = serializers.CharField(max_length=255, allow_null=True)
    experience = serializers.ChoiceField(choices=ProfessionalDetailsSection.EXPERIENCE_CHOICES)
    qualification = serializers.PrimaryKeyRelatedField(queryset=Qualification.objects.all(), required=False, allow_null=True)
    state_job_place = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(), required=False, allow_null=True)
    country_job_place = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=False, allow_null=True)

    class Meta:
        model = InstructorProfile
        fields = [
            'phone',
            'date_of_birth',
            'gender',
            'occupation',
            'area_job_place',
            'experience',
            'qualification',
            'state_job_place',
            'country_job_place',
        ]

    def validate(self, data):
        user_profile = self.context['request'].user.userprofile
        print("User Profile ::: 🙌🙌", user_profile)
        if not user_profile.just_created:
            raise ValidationError("User profile create only works one time after signup .")
        
        return data

    def create(self, validated_data):
        user_profile = self.context['request'].user.userprofile

        # Update the UserProfile fields
        user_profile.phone = validated_data.get('phone', user_profile.phone)
        user_profile.date_of_birth = validated_data.get('date_of_birth', user_profile.date_of_birth)
        user_profile.gender = validated_data.get('gender', user_profile.gender)
        user_profile.just_created = False
        user_profile.save()


        # Create the ProfessionalDetailsSection
        professional_details = ProfessionalDetailsSection.objects.create(
            user_profile = user_profile,
            occupation=validated_data.get('occupation'),
            area_job_place=validated_data.get('area_job_place'),
            experience=validated_data.get('experience'),
            qualification=validated_data.get('qualification'),
            state_job_place = validated_data.get('state_job_place'),
            country_job_place = validated_data.get('country_job_place'),
        )


        # Create the InstructorProfile
        instructor_profile = InstructorProfile.objects.create(
            user_profile=user_profile,
            # address=user_address,
            professional_details=professional_details,
        )

        return instructor_profile
