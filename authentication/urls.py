from django.urls import path
from .views.admin_auth import AdminLogin
from .views.refresh_token import TokenRefresh
from .views.user_auth import (
    UserSignUpView,
    UserLoginView,
    VerifyEmail
)

urlpatterns = [
    #Admin login
    path('admin-login/', AdminLogin.as_view(), name='admin_login'),

    #User auth
    path('user-signup/', UserSignUpView.as_view(), name='user-signup(student/instructor)'),
    path('user-login/', UserLoginView.as_view(), name='user-login(student/instructor)'),
    path('verify-email-otp/', VerifyEmail.as_view(), name='verfiy-email(student/instructor)'),

    # Refresh token
    path('token/refresh/', TokenRefresh.as_view(), name='token_refresh'),
]
