from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import permissions as per, viewsets, status, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .filters import ProductFilter
from .models import Product, Category, MainComment
from .serializers import ProductSerializer, CategorySerializer, CreateUpdateProductSerializer, \
    MainCommentSerializer, ProductListSerializer
from .permissions import IsOwner, IsAuthor


class MyPagination(PageNumberPagination):
    """Пагинация"""
    page_size = 1


class ProductViewSet(viewsets.ModelViewSet):
    """Класс продукта с помощью которого можно делать CRUD"""
    pagination_class = MyPagination
    queryset = Product.objects.all()
    filter_class = ProductFilter
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        if self.action == 'retrieve':
            return ProductSerializer
        else:
            return CreateUpdateProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:
            permissions = []
        else:
            permissions = [per.IsAdminUser]
        return [permission() for permission in permissions]

    @action(methods=['get'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        if q is not None:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryList(ListAPIView):
    """Лист катеорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MainCommentViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    queryset = MainComment.objects.all().order_by('-created')
    serializer_class = MainCommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            permission = [IsAuthor]
        else:
            permission = [per.IsAuthenticated, ]
        return [permission() for permission in permission]