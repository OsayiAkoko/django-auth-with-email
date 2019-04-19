from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
]
