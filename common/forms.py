from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserChangeForm




#메타 안에 있는 모델과 필드들을 커스텀 유저에 맞게 수정 작업하는 것
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username', 'password1', 'password2', 'email',
                 'semester', 'lastgpa', 'fullgpa'
                 ,'income','departments','residence']


class CustomCsUserChangeForm(UserChangeForm):
    password = None
    fullgpa = forms.CharField(label='성적', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'8',}),
    )


    class Meta:
        model = User()
        fields = ['fullgpa']

