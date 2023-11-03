from django.urls import path, include
from users import views
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('dummy_page/', views.dummy_page, name='dummy_page'),

    # path('password_change/', PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'), # tried this but didn't work

    # include Django's authentication system (login, logout, password change, password reset, etc.) in the users app
    path('accounts/', include('django.contrib.auth.urls')),
]
