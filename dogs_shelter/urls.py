from rest_framework.routers import DefaultRouter

from .views import DogViewSet, BreedViewSet, CuratorViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'dogs', DogViewSet)
router.register(r'breeds', BreedViewSet)
router.register(r'curators', CuratorViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = router.urls
