from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, product_list
from django.urls import path

router = DefaultRouter()
router.register('', ProductViewSet)

# concatenate router-generated urls with any additional html view
urlpatterns = router.urls + [
    path('', product_list, name='product_list'),
]
