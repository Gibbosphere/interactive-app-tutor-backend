# from django.urls import path
# from . import views

# urlpatterns = [
#     path('api/tutorials/', views.tutorial_list, name='tutorial-list'),
# ]


# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InteractiveGuideViewSet, InfoIconViewSet, TutorialViewSet, DocumentationViewSet

router = DefaultRouter()
router.register(r'api/interactive-guides', InteractiveGuideViewSet)
router.register(r'api/info-icons', InfoIconViewSet)
router.register(r'api/tutorial', TutorialViewSet)
router.register(r'api/documentation', DocumentationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
