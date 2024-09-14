import nested_admin
from django import forms
from django.contrib import admin
from django.forms import ValidationError
from .models import InteractiveGuide, TooltipInteractiveGuide, TooltipTutorial, TutorialStage, TestTask, InfoIcon, ClickElement, TextInputElement, DocumentationPage

# Help Icons and Documentation 
admin.site.register(InfoIcon)
admin.site.register(DocumentationPage)

# Interactive Guides
class TooltipInteractiveGuideInline(nested_admin.NestedTabularInline):
    model = TooltipInteractiveGuide
    extra = 1
    min_num = 1
    can_delete = True

class InteractiveGuideAdmin(nested_admin.NestedModelAdmin):
    inlines = [TooltipInteractiveGuideInline]

admin.site.register(InteractiveGuide, InteractiveGuideAdmin)


# Tutorials
class TextInputElementInline(nested_admin.NestedTabularInline):
    model = TextInputElement
    extra = 1
    can_delete = True
    min_num = 0

class ClickElementInline(nested_admin.NestedTabularInline):
    model = ClickElement
    extra = 1
    can_delete = True
    inlines = [TextInputElementInline]
    min_num = 1

class TestTaskInline(nested_admin.NestedStackedInline):
    model = TestTask
    extra = 1
    can_delete = True
    inlines = [ClickElementInline]
    min_num = 0

class TooltipTutorialInline(nested_admin.NestedTabularInline):
    model = TooltipTutorial
    extra = 1
    can_delete = True
    min_num = 1

class TutorialStageAdmin(nested_admin.NestedModelAdmin):
    inlines = [TooltipTutorialInline, TestTaskInline]

    def save_model(self, request, obj, form, change):
        """Ensure each TutorialStage has at least one TooltipTutorial."""
        super().save_model(request, obj, form, change)
        if obj.tooltips.count() < 1:
            raise ValidationError('Each tutorial stage must have at least one tooltip.')

admin.site.register(TutorialStage, TutorialStageAdmin)