from rest_framework import generics
from passwords.models import Password
from passwords.serializers import PasswordSerializer

class PasswordListCreateView(generics.ListCreateAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer

class PasswordRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
