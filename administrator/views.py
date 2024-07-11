from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin

# Create your views here.
from core.models import User, Product
from common.authentication import JWTAuthentication
from common.serializers import UserSerializer
from administrator.serializers import ProductSerializer

class AmbassadorAPIView(APIView):
    def get(self, _):
        ambassadors = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassadors, many=True)
        return Response(serializer.data)


class ProductGenericAPIView(GenericAPIView, ListModelMixin, RetrieveModelMixin,CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        
        return self.list(request) 
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, pk=None):
        return self.partial_update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)