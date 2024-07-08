from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView

app_name = 'common'

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login')
]
