from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomViewSet(viewsets.ViewSet):
    """
    A ViewSet without a model, handling custom API responses.
    """

    def list(self, request):
        """
        Handle GET requests at /custom/
        """
        data = {"message": "Hello from the custom ViewSet!"}
        return Response(data)

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        """
        Custom endpoint: Handle GET requests at /custom/custom_action/
        """
        return Response({"message": "This is a custom action!"})