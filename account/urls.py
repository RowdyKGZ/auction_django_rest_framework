from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import RegisterView, ActivationView, \
    LoginView, LogoutView, ProfileViewSet


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/<int:pk>/', ProfileViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'put': 'update'
    }))
]