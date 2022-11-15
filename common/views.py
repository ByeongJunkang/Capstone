from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.forms import RegisterForm

from .forms import CustomCsUserChangeForm
from .models import User
from .serializers import UserSerializer



class RegistrationAPIView(APIView):
    permission_classes(AllowAny)
    def post(self, request):

        user_serializer = UserSerializer(data=request.data) #Request의 data를 UserSerializer로 변환
        if user_serializer.is_valid():
            user_serializer.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(user_serializer.data, status=status.HTTP_201_CREATED) 
        
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
class UserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


#홈페이지 회원가입
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







