from django.db import models
from metacontent.models.country import Country
from metacontent.models.state import State
from metacontent.models.qualification import Qualification
from django.utils import timezone
from userprofile.models.user_profile import UserProfile
import uuid


class ProfessionalDetailsSection(models.Model):
    EXPERIENCE_CHOICES = [
        ('0-1', '0-1 years'),
        ('1-3', '1-3 years'),
        ('3-5', '3-5 years'),
        ('5+', '5+ years'),
    ]
    # CharField secion ==================
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255)
    area_job_place = models.CharField(max_length=255)
    experience = models.CharField(max_length=5, choices=EXPERIENCE_CHOICES)

    #  Foriegn key secion ==================
    qualification = models.ForeignKey(Qualification, on_delete=models.SET_NULL, null=True, blank=True)
    state_job_place = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    country_job_place = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)  


    def __str__(self):
        return f"{self.occupation} at {self.area_job_place}, {self.state_job_place}, {self.country_job_place}"
