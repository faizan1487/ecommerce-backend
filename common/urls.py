from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, UserAPIView, LogoutAPIView

app_name = 'common'

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('user', UserAPIView.as_view(), name='user')
]
