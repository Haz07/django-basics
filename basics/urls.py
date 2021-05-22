from django.urls import path, include
from . import views
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('article/', views.article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('article/<int:pk>/', views.article_detail)
    path('article/<int:id>/', ArticleDetails.as_view()),
    path('garticle/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]