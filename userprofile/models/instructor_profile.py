from django.db import models
import uuid

from userprofile.models.user_profile import (
    UserProfile,
    UserImage
)

from userprofile.models.professional_details import ProfessionalDetailsSection


class InstructorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    professional_details = models.OneToOneField(ProfessionalDetailsSection, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.user.username}'s Instructor Profile"


