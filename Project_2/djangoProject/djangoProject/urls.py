"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from cars import views

urlpatterns = [
    path('cars/', include('cars.urls')),
    path('admin/', admin.site.urls),
    path('profile/', views.EditUser.as_view(), name='profile'),
    path('password/', views.PasswordChange.as_view(), name='password'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('delete/', views.delete_user_request, name='delete'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        views.PasswordResetConfirm.as_view(),
        name='password_reset_confirm'
    ),
]
