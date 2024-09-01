from django.urls import path
from .views import (
    InstructorProfileView,
    InstructorProfileUpdate,
    InstructorProfessionalDetailUpdate,
    InstructorProfessionalDetailUpdate,
    InstructorProfileDetails
    )

urlpatterns = [
    #Admin login
    path('instructor-profile/create/', InstructorProfileView.as_view(), name='instructor_profile_create'),
    path('instructor-profile/update/', InstructorProfileUpdate.as_view(), name='instructor_profile_update'),
    path('instructor-profile/professional-details/update/', InstructorProfessionalDetailUpdate.as_view(), name='instructor_profile_professional_update'),
    path('instructor-profile/details/', InstructorProfileDetails.as_view(), name='instructor_profile_professional_update'),

]
