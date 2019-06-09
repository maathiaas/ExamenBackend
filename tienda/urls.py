from rest_framework import routers
from .viewsets import ClienteViewSets

router = routers.SimpleRouter()
router.register('cliente', ClienteViewSets)




urlpatterns = router.urls