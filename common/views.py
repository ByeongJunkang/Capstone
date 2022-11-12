from django.contrib.auth import authenticate, login

from common.forms import RegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import CustomCsUserChangeForm




def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'common/signup.html', {'form': form})


def show(request):
    user = get_object_or_404(User)
    context = {'user': user}
    return render(request, 'common/user.html', context)

# users/views.py


def profile_view(request):
    if request.method == 'GET':
        return render(request, 'common/user.html')



def profile_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomCsUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            return render(request, 'common/user.html')
    else:
        user_change_form = CustomCsUserChangeForm(instance = request.user)

        return render(request, 'common/profile_update.html', {'user_change_form':user_change_form})







