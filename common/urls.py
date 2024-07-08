from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, UserAPIView

app_name = 'common'

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('user', UserAPIView.as_view(), name='user')
]
