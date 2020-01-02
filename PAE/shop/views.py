from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import UserInfo
from .forms import ChangeUserInfoForm

# Create your views here.

def index(request):
    return render(request, 'shop/12.html')

class PromoLoginView(LoginView):
    template_name = 'shop/login.html'

@login_required
def profile_info(request):
    return render(request, 'shop/profile_info.html')


class PromoLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'shop/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = UserInfo
    template_name = 'shop/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('shop:profile_info')
    success_message = 'Личные данные пользователя изменены.'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
