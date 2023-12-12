from django.urls import path,include,reverse_lazy
from .views import dashboard,profile_list,profile
from django.contrib.auth import views as auth_views

app_name="dwitter"

urlpatterns=[
    path("",dashboard,name="dashboard"),
    path("profile_listing",profile_list,name="profile_list"),
    path("profile/<int:pk>",profile,name="profile"),
    path("accounts/",include("django.contrib.auth.urls")),
    path("logout",auth_views.logout_then_login,name="logout"),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),

  ]