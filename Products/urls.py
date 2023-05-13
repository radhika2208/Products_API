from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Products', views.ProductViewSet, basename='Products')
urlpatterns = [
    path('', views.Index, name="Index"),
    path('', include(router.urls)),
]