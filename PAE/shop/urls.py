from django.urls import path, include

from .views import index, PromoLoginView, profile_info, PromoLogoutView, ChangeUserInfoView, PromoPasswordChangeView

from .views import RegisterUserView, RegisterDoneView
from .views import user_activate

app_name = 'shop'
urlpatterns = [
    path('', index, name="index"),
    path('login/', PromoLoginView.as_view(), name = 'login'),
    path('accounts/profile/', profile_info, name = 'profile_info'),
    path('accounts/logout/', PromoLogoutView.as_view(), name = 'profile_logout'),
    path('account/profile/change/', ChangeUserInfoView.as_view(), name = 'change_user_info'),
    path('accounts/password_change/', PromoPasswordChangeView.as_view(), name = 'password_change'),
    path('accounts/register/activate/<str:sign>/', user_activate, name = 'user_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name = 'register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name = 'register_user'),
]
