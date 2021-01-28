from rest_framework import viewsets, mixins, permissions

from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOwnerUser


class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                   mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Класс для ордера"""
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerUser]
    serializer_class = OrderSerializer

    def get_queryset(self):
        # queryset = super().self.get_queryset()
        user = self.request.user
        return Order.objects.filter(user=user)
