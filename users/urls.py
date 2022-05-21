from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import *
app_name="user"
urlpatterns = [
    path("login", views.login_view, name="login" ),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
