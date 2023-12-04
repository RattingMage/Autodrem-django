from django.urls import path
from authenticate.views import RegistrationView, LoginView, ProfileView, UpdatePasswordView, CarListCreateView, \
    CarDetailView

urlpatterns = [
    path('signup/', RegistrationView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('update_password/', UpdatePasswordView.as_view(), name="update_password"),

    path('cars/', CarListCreateView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]