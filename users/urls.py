from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, VerifiedEmailView, ProfileView, ConfirmUserView, \
    ConfirmUserErrorView, generate_new_password, UserUpdateView, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('ban/', BanView.as_view(), name='ban'),

    path('register/', RegisterView.as_view(), name='register'),
    path('users/verified_email/', VerifiedEmailView.as_view(), name='verified_email'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='users_profile'),

    # path('confirm_email/<str:token>/', ConfirmEmailView.as_view(), name='confirm_email'),

    path('confirm_user/', ConfirmUserView.as_view(), name='confirm_user'),
    path('confirm_user_error/', ConfirmUserErrorView.as_view(), name='confirm_user_error'),

    path('profile/generate_password/', generate_new_password, name='generate_new_password'),

    path('user_list/', UserListView.as_view(), name='user_list'),
]
