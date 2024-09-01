from django.contrib import admin
from .models import (
    UserProfile,
    InstructorProfile
)


@admin.register(UserProfile)
class UserProfileDisplay(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'user_type',
        'just_created',
        'gender',
        'date_of_birth',
        'alternate_email',
        'alternate_phone',
    )


@admin.register(InstructorProfile)
class InstructorProfileDisplay(admin.ModelAdmin):
    list_display = (
        'id',
        'get_user_profile',

        'get_professional_details',
    )
    
    readonly_fields = (
        'get_user_profile',
        'get_professional_details',
    )

    def get_user_profile(self, obj):
        return obj.user_profile.user.username

    def get_professional_details(self, obj):
        return f"{obj.professional_details.occupation}, {obj.professional_details.experience}"

    get_user_profile.short_description = 'User Profile'

    get_professional_details.short_description = 'Professional Details'


