from rest_framework import viewsets
from . import models
from . import serializers
from .permissions import IsOwner
# Create your views here.

class FriendViewset(viewsets.ModelViewSet):
    permissions_classes = [IsOwner]
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer

class BelongingViewset(viewsets.ModelViewSet):
    permissions_classes = [IsOwner]
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer

class BorrowedViewset(viewsets.ModelViewSet):
    permissions_classes = [IsOwner]
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer