from rest_framework import serializers
from .models import InteractiveGuide, TooltipInteractiveGuide, TooltipTutorial, InfoIcon, TutorialStage, TestTask, ClickElement, TextInputElement, DocumentationPage

# Interactive Guides
class TooltipInteractiveGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TooltipInteractiveGuide
        fields = '__all__'

class InteractiveGuideSerializer(serializers.ModelSerializer):
    tooltips = TooltipInteractiveGuideSerializer(many=True)

    class Meta:
        model = InteractiveGuide
        fields = '__all__'


# Tutorial
class TooltipTutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TooltipTutorial
        fields = '__all__'

class TextInputElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextInputElement
        fields = '__all__'

class ClickElementSerializer(serializers.ModelSerializer):
    text_input_elements = TextInputElementSerializer(many=True)

    class Meta:
        model = ClickElement
        fields = '__all__'

class TestTaskSerializer(serializers.ModelSerializer):
    click_elements = ClickElementSerializer(many=True)

    class Meta:
        model = TestTask
        fields = '__all__'

class TutorialStageSerializer(serializers.ModelSerializer):
    tooltips = TooltipTutorialSerializer(many=True)
    test_tasks = TestTaskSerializer(many=True)

    class Meta:
        model = TutorialStage
        fields = '__all__'


# Info Icons
class InfoIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoIcon
        fields = '__all__'


# Documentation
class DocumentationPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentationPage
        fields = '__all__'
