from rest_framework import serializers
from django.contrib.auth.models import User
from userprofile.models.user_profile import (
    UserProfile,
    OtpValidation
    )
from authentication.constants import ROLE_CHOICES
from userprofile.constants import (
    GENDER_CHOICES, 
    # GENDER_NOT_SPECIFY,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError
from utils.generate_otp import generate_otp
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'is_superuser', 
            'is_active', 
            'date_joined'
        )

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'user', 
            'user_type', 
            'phone', 
            'alternate_email', 
            'alternate_phone', 
            'date_of_birth', 
            'gender',
            'just_created',
        )


class UserLoginSerializer(TokenObtainPairSerializer):
    """
    User login serializer setup
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        try:
            user = User.objects.get(username=username)
            if not User.is_active:
                raise ValidationError({"message": "User  is not valid. Please contact admin panel"})
            

            if not user.check_password(password):
                raise ValidationError({'message': 'Please check your password'})

            if not user.is_active:
                raise ValidationError({'message': 'Your account is not activated'})

        except User.DoesNotExist:
            raise ValidationError({'message': 'Please check your username'})

        user = authenticate(username=username, password=password)
        self.user = user

        data = super().validate(attrs)

        try:
            user_profile = UserProfile.objects.get(user=user)
            data['is_active'] = user_profile.user.is_active
            data['user_type'] = user_profile.user_type
            
            data['message'] = "User login successfull !"
        except UserProfile.DoesNotExist:
            data['user_profile'] = None
            data['message'] = "User profile not found. Please complete your profile."

        return data


class SignUpSerializer(serializers.Serializer):
    """
    User signup serializer setup
    """
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=255)
    user_type = serializers.ChoiceField(choices=ROLE_CHOICES)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, allow_blank=True, required=False)

    def validate_password(self, value):
        """
        Validate password to ensure it meets the required criteria.
        """
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("Password must contain at least one letter.")
        return value

    def validate(self, data):
        """
        Validate username and email for uniqueness.
        """
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError({"username":"Username is already taken."})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email":"Email is already taken."})
        return data

    # def to_internal_value(self, data):
    #     """
    #     Override to_internal_value to handle error formatting during validation.
    #     """
    #     try:
    #         return super().to_internal_value(data)
    #     except serializers.ValidationError as exc:
    #         for field, errors in exc.detail.items():
    #             raise serializers.ValidationError({"message": errors[0]})



    def create(self, validated_data):
        """
        Create a new user and associated profile.
        """
        if User.objects.filter(username = validated_data['username']).exists():
            raise ValidationError({"message":"username is already taken."})

        otp = generate_otp()


        print(otp)
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data.get('last_name', ''),
            email=validated_data['email'],
            password=validated_data['password'],
            is_active = False
        )
        UserProfile.objects.create(
            user=user,
            gender=validated_data['gender'],
            user_type=validated_data['user_type'],
            otp = otp
        )
        OtpValidation.objects.create(
            user=user,
            otp=otp
        )
        

        context = {
            'user':user,
            'otp':otp
        }
        html_message = render_to_string('mail_verify.html', context)
        plain_text = strip_tags(html_message)

        send_mail(
            "Wellcome to EduPort. Verify your email.",
            plain_text,
            settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            html_message=html_message,
            fail_silently=False
        )

        return user


