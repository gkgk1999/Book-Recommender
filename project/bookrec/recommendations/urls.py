from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookRecommendationViewSet, search_books, like_recommendation, add_comment

router = DefaultRouter()
router.register(r'recommendations', BookRecommendationViewSet)

urlpatterns = [
    path('search/', search_books, name='search_books'),
    path('recommendations/<int:pk>/like/', like_recommendation, name='like_recommendation'),
    path('recommendations/<int:pk>/comment/', add_comment, name='add_comment'),
    path('', include(router.urls)),
]
