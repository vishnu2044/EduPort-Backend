from rest_framework import serializers
from userprofile.models import (
    UserProfile,
    ProfessionalDetailsSection
)
from metacontent.models import (
    Qualification,
    State,
    Country
)

class InstructorProfileUpdateSerialzer(serializers.ModelSerializer):
    # User model
    first_name = serializers.CharField(max_length = 255, required=False, allow_null=True)
    last_name = serializers.CharField(max_length = 255, required=False, allow_null=True)

    # UserProfile model
    phone = serializers.CharField(max_length = 15, required=False, allow_null=True)
    alternate_email = serializers.EmailField(max_length = 255, required=False, allow_null=True)
    alternate_phone = serializers.CharField(max_length = 15, required=False, allow_null=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = UserProfile
        fields = [
            'first_name', 'last_name',
            'phone', 'alternate_email', 'alternate_phone',
            'date_of_birth'
        ]
    
    def validate_phone(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("Phone number should be 10 digits")
        
        if UserProfile.objects.filter(phone=value).exclude(user=self.context['request'].user).exists():
            raise serializers.ValidationError("Phone number already taken")
        
        return value
    
    def validate_alternate_phone(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("Phone number should be 10 digits")
        
        if UserProfile.objects.filter(alternate_phone=value).exclude(user=self.context['request'].user).exists():
            raise serializers.ValidationError("Phone number already taken")   

        return value     
    
    def validate_alternate_phone(self, value):
        if value and len(value) != 10:
            raise serializers.ValidationError("Phone number should be 10 digits")
        
        if UserProfile.objects.filter(alternate_phone=value).exclude(user=self.context['request'].user).exists():
            raise serializers.ValidationError("Phone number already taken")   

        return value     

    def update(self, instance, validated_data):
        user = self.context['request'].user

        #update user model fields
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.save()

        # Update the UserProfile fields
        instance.phone = validated_data.get('phone', instance.phone)
        instance.alternate_email = validated_data.get('alternate_email', instance.alternate_email)
        instance.alternate_phone = validated_data.get('alternate_phone', instance.alternate_phone)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()

        return user


class InstructorProfileProfessionalUpdate(serializers.ModelSerializer):

    occupation = serializers.CharField(max_length = 255, required=False, allow_null=True)
    area_job_place = serializers.CharField(max_length = 255, required=False, allow_null=True)
    experience = serializers.ChoiceField(choices=ProfessionalDetailsSection.EXPERIENCE_CHOICES, required=False, allow_null=True)

    qualification = serializers.PrimaryKeyRelatedField(queryset=Qualification.objects.all(), required=False, allow_null=True)
    state_job_place = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(), required=False, allow_null=True)
    country_job_place = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=False, allow_null=True)

    class Meta:
        model = ProfessionalDetailsSection
        fields = [
            'occupation', 'area_job_place', 'experience',
            'qualification', 'state_job_place', 'country_job_place'
        ]

    def update(self, instance, validated_data):
        instance.occupation = validated_data.get('occupation', instance.occupation)
        instance.area_job_place = validated_data.get('area_job_place', instance.area_job_place)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.qualification = validated_data.get('qualification', instance.qualification)
        instance.state_job_place = validated_data.get('state_job_place', instance.state_job_place)
        instance.country_job_place = validated_data.get('country_job_place', instance.country_job_place)
        instance.save()

        return instance