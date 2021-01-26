from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, CategoryList, CommentCreate

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryList.as_view()),
    path('comments/create', CommentCreate.as_view()),
]
