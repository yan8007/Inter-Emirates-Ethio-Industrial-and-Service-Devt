from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    CustomUserViewSet, 
    UserRegistrationView,
    UserProfileView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    UserRoleUpdateView,
    UserStatusToggleView
)

# Create a router for user-related viewsets
router = DefaultRouter()
router.register(r'', CustomUserViewSet, basename='users')

urlpatterns = [
    # Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # User Registration and Management
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    
    # Password Management
    path('password/reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # Role and Status Management
    path('role/update/', UserRoleUpdateView.as_view(), name='user_role_update'),
    path('status/toggle/', UserStatusToggleView.as_view(), name='user_status_toggle'),
    
    # Include ViewSet routes
    path('', include(router.urls))
]