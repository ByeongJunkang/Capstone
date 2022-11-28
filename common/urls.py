from django.urls import path
from django.contrib.auth import views as auth_views
from common import views
from django.conf.urls import include
from rest_framework import routers
from .views import *

from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'common'
router = routers.DefaultRouter()
router.register('list', UserViewSet) # 유저리스트 (테스트용)
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('show/', views.profile_view, name = 'show'),
    path('show/update/', views.profile_update_view, name='profile_update'),
    path('users/', views.RegisterAPIView.as_view(), name='api_user'),
    path("auth/", views.AuthAPIView.as_view()),
    path("auth/update/",views.UpdateProfile.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("", include(router.urls)),

]