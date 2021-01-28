from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, CategoryList, MainCommentViewSet

router = DefaultRouter()
router.register('main-comments', MainCommentViewSet)
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryList.as_view()),
]
