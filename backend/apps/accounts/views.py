from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import extend_schema, inline_serializer
from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=inline_serializer(
            name='LoginRequest',
            fields={
                'username': serializers.CharField(),
                'password': serializers.CharField(),
            }
        ),
        responses={200: UserSerializer}
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(UserSerializer(user).data)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=None,
        responses={200: inline_serializer(name='LogoutResponse', fields={'detail': serializers.CharField()})}
    )
    def post(self, request):
        logout(request)
        return Response({'detail': 'Successfully logged out.'})


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
