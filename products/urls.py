from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_list
from django.urls import path

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = router.urls 
urlpatterns+= [
    path('', product_list, name='product_list'),
]