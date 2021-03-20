from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('friends', views.FriendViewset)
router.register('belongings', views.BelongingViewset)
router.register('borrowings', views.BorrowedViewset)

urlpatterns = router.urls