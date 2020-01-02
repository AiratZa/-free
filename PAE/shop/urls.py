from django.urls import path, include

from .views import index, PromoLoginView, profile_info, PromoLogoutView, ChangeUserInfoView

app_name = 'shop'
urlpatterns = [
    path('', index, name="index"),
    path('login/', PromoLoginView.as_view(), name = 'login'),
    path('accounts/profile/', profile_info, name = 'profile_info'),
    path('accounts/logout/', PromoLogoutView.as_view(), name = 'profile_logout'),
    path('account/profile/change', ChangeUserInfoView.as_view(), name = 'change_user_info'),
]
