from django.urls import path, include

from .views import index, PromoLoginView, profile_info, PromoLogoutView, ChangeUserInfoView, PromoPasswordChangeView

from .views import RegisterUserView, RegisterDoneView
from .views import user_activate

from .views import DeleteUserView

from django.contrib.auth.views import PasswordChangeView


from .views import by_category, shop, list_by_category, list_by_shop
app_name = 'shop'
urlpatterns = [
    path('', index, name="index"),
    path('by_category/<int:pk>/', by_category, name = 'by_category'),
    path('shop/<str:name>/', shop, name = 'shop'),
    path('by_category/', list_by_category, name = 'list_by_category'),
    path('by_shop/', list_by_shop, name = 'list_by_shop'),
    path('login/', PromoLoginView.as_view(), name = 'login'),
    path('account/profile/change/', ChangeUserInfoView.as_view(), name = 'change_user_info'),
    path('account/profile/delete/', DeleteUserView.as_view(), name = 'delete_user'),
    path('accounts/profile/', profile_info, name = 'profile_info'),
    path('accounts/logout/', PromoLogoutView.as_view(), name = 'profile_logout'),
    path('accounts/password_change/', PromoPasswordChangeView.as_view(), name = 'password_change'),
    path('accounts/register/activate/<str:sign>/', user_activate, name = 'user_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name = 'register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name = 'register_user'),

]
