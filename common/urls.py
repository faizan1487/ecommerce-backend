from django.urls import path, include
from .views import RegisterAPIView

app_name = 'common'

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register')
]
