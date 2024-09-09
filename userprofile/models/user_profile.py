from django.db import models
from django.contrib.auth.models import User
from userprofile.constants import (
    GENDER_CHOICES,
    GENDER_NOT_SPECIFY
)
from authentication.constants import (
    ROLE_CHOICES,
    ROLE_ADMIN,
)
import uuid
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from datetime import timedelta


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=ROLE_CHOICES, default=ROLE_ADMIN)
    alternate_email = models.EmailField(max_length=255, null=True, blank=True)
    alternate_phone = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=GENDER_NOT_SPECIFY)
    just_created = models.BooleanField(default=True)
    otp = models.CharField(max_length=6, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.user.username}'s Profile"


class UserImage(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    profile_img = models.ImageField(
        upload_to='user-profile/profile-img/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        blank=True, 
        null=True
    )
    cover_img = models.ImageField(
        upload_to='user-profile/cover-img/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        blank=True, 
        null=True
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Images"

    class Meta:
        verbose_name = "User Image"
        verbose_name_plural = "User Images"



class OtpValidation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when OTP is created
    updated_at = models.DateTimeField(auto_now=True)  

    def is_otp_valid(self):
        """
        Check if the OTP is still valid. OTP is valid for 2 minutes from creation.
        """
        expiration_time = self.updated_at + timedelta(minutes=1)
        return timezone.now() < expiration_time

    def __str__(self):
        return f"OTP for {self.user.username} - {self.otp}"

