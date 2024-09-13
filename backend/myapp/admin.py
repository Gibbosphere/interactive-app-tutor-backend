from django.contrib import admin
from django.forms import ValidationError
from .models import InteractiveGuide, TooltipInteractiveGuide, TooltipTutorial, TutorialStage, TestTask, InfoIcon, ClickElement, TextInputElement, DocumentationPage

# Help Icons and Documentation 
admin.site.register(InfoIcon)
admin.site.register(DocumentationPage)

# Interactive Guides
# Define an inline admin descriptor for TooltipInteractiveGuide
class TooltipInteractiveGuideInline(admin.TabularInline):
    model = TooltipInteractiveGuide
    extra = 1  # How many extra empty tooltips to display by default
    min_num = 1  # At least one TooltipInteractiveGuide per InteractiveGuide
    can_delete = True

# Define a custom admin for InteractiveGuide that includes TooltipInteractiveGuideInline
class InteractiveGuideAdmin(admin.ModelAdmin):
    inlines = [TooltipInteractiveGuideInline]  # Include tooltips directly under each InteractiveGuide

    def save_model(self, request, obj, form, change):
        """Override the save_model method to enforce the rule that each guide must have at least one tooltip."""
        super().save_model(request, obj, form, change)
        if obj.tooltips.count() < 1:  # Check if the InteractiveGuide has less than one Tooltip
            raise ValidationError('Each interactive guide must have at least one tooltip.')

admin.site.register(InteractiveGuide, InteractiveGuideAdmin)

# Tutorial
# Inline for TextInputElement (Optional for ClickElement)
class TextInputElementInline(admin.TabularInline):
    model = TextInputElement
    extra = 1
    can_delete = True
    min_num = 0  # A ClickElement can have zero or more TextInputElements

# Inline for ClickElement (Mandatory for TestTask)
class ClickElementInline(admin.TabularInline):
    model = ClickElement
    extra = 1
    can_delete = True
    inlines = [TextInputElementInline]  # This inline will not show directly here, we'll manage it separately
    min_num = 1  # A TestTask must have at least one ClickElement

# Inline for TestTask (Optional for TutorialStage)
class TestTaskInline(admin.StackedInline):  # Switching to StackedInline for a clearer layout
    model = TestTask
    extra = 1
    can_delete = True
    min_num = 0  # A TutorialStage can have zero or more TestTasks

# Inline for TooltipTutorial (Mandatory for TutorialStage)
class TooltipTutorialInline(admin.TabularInline):
    model = TooltipTutorial
    extra = 1
    can_delete = True
    min_num = 1  # A TutorialStage must have at least one TooltipTutorial

# Separate admin for ClickElement to manage TextInputElements
class ClickElementAdmin(admin.ModelAdmin):
    inlines = [TextInputElementInline]  # TextInputElements for each ClickElement

# Define custom admin for TutorialStage with related inlines
class TutorialStageAdmin(admin.ModelAdmin):
    inlines = [TooltipTutorialInline, TestTaskInline]  # Direct inlines for tooltips and test tasks

    def save_model(self, request, obj, form, change):
        """Override the save_model method to enforce the rule that each TutorialStage must have at least one TooltipTutorial."""
        super().save_model(request, obj, form, change)
        if obj.tooltips.count() < 1:  # Ensure TutorialStage has at least one TooltipTutorial
            raise ValidationError('Each tutorial stage must have at least one tooltip.')

admin.site.register(TutorialStage, TutorialStageAdmin)
admin.site.register(ClickElement, ClickElementAdmin)