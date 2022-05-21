from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "user"

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
