from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import InteractiveGuide, TooltipInteractiveGuide, TooltipTutorial, InfoIcon, TutorialStage, TestTask, ClickElement, DocumentationPage
from .serializers import InteractiveGuideSerializer, InfoIconSerializer, TutorialStageSerializer, DocumentationPageSerializer

class InteractiveGuideViewSet(viewsets.ModelViewSet):
    queryset = InteractiveGuide.objects.prefetch_related('tooltips').distinct()
    serializer_class = InteractiveGuideSerializer
    filter_backends = [OrderingFilter]  # Add ordering filter
    # ordering_fields = ['tooltips__position']  # Define ordering field
    # ordering = ['tooltips__position']  # Apply default ordering by tooltips position

class InfoIconViewSet(viewsets.ModelViewSet):
    queryset = InfoIcon.objects.all()
    serializer_class = InfoIconSerializer

class TutorialViewSet(viewsets.ModelViewSet):
    queryset = TutorialStage.objects.prefetch_related('tooltips', 'test_tasks__click_elements').distinct()
    serializer_class = TutorialStageSerializer
    filter_backends = [OrderingFilter]
    # ordering_fields = ['tooltips__position', 'test_tasks__position', 'test_tasks__click_elements__position']
    # ordering = ['tooltips__position', 'test_tasks__position', 'test_tasks__click_elements__position']  # Apply ordering using the position value

class DocumentationViewSet(viewsets.ModelViewSet):
    queryset = DocumentationPage.objects.all()
    serializer_class = DocumentationPageSerializer