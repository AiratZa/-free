from django import forms

from .models import UserInfo

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label = 'Адрес электронной почты')

    class Meta:
        model = UserInfo
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'send_messages')