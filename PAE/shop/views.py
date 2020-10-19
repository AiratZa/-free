from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import UserInfo
from .forms import ChangeUserInfoForm, RegisterUserForm


from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateView

from django.core.signing import BadSignature
from .utilities import signer

from django.contrib.auth import logout
from django.contrib import messages

from .models import Shop

import json
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'shop/main_page.html')

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


class PromoPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'shop/password_change.html'
    success_url = reverse_lazy('shop:profile_info')
    success_message = 'Пароль пользователя изменен'

class RegisterUserView(CreateView):
    model = UserInfo
    template_name = 'shop/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('shop:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'shop/register_done.html'




def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(UserInfo, username = username)
    if user.is_activated:
        template = 'shop/user_is_activated.html'
    else:
        template = 'shop/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

class DeleteUserView(DeleteView):
    model = UserInfo
    template_name = 'shop/delete_user.html'
    success_url = reverse_lazy('shop:index')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 
                             'Пользователь удален')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset = None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk = self.user_id)


def by_category (request, pk):
    pass
def shop(request, name):
    context = {}
    context['shop'] = get_object_or_404(Shop, name = name)
    return render(request, 'shop/shop.html', context)

def list_by_category (request):
    pass

def list_by_shop(request):
    context = {}
    context['shops'] = list(Shop.objects.order_by('name').values())
    context['json_list'] = json.dumps(context['shops'])

    return render(request, 'shop/list_by_shop.html', context)
