from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib import messages
from .models import User
from users.forms import UserForm, PasswordResetForm
from . import models
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request, "users/login.html" )

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):
    if request.method =="POST":
        print(111, request.POST) 
        profile_img = request.FILES["profile_img"]
        username = request.POST["username"]
        password = request.POST["password"]
        firstname= request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]
        user=User.objects.create_user(username, email, password)
        user.firstname = firstname
        user.lastname = lastname
        user.student_id = student_id
        user.profile_img = profile_img
        user.save()
        return redirect("user:login")
    return render(request, "users/signup.html")


class PasswordResetView(auth_views.PasswordResetView):
    """
    비밀번호 초기화 - 사용자ID, email 입력
    """
    template_name = 'users/password_reset.html'
    # success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    email_template_name = 'registration/password_reset_email.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    비밀번호 초기화 - 메일 전송 완료
    """
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    비밀번호 초기화 - 새로운 비밀번호 입력
    """
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('login')

# todo password_reset_email.html 템플릿 파일 만들기
