# users/urls.py
from django.urls import path, include
from .views import (
    UserViewSet,
    RegisterView,
    TokenView,
    PaymentViewSet,
    StripePaymentView,
    CustomTokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"register", RegisterView, basename="register")
router.register(r"payments", PaymentViewSet)

urlpatterns = [
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
    path("stripe-payment/", StripePaymentView.as_view(), name="stripe_payment"),
]
