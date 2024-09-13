from django.db import models

# Interactive guides
class InteractiveGuide(models.Model):
    name = models.CharField(max_length=255)
    starting_page = models.CharField(max_length=255)

    def __str__(self):
        return self.name

TYPE_CHOICES = [
    ('informative', 'Informative'),
    ('action', 'Action'),
]
class TooltipInteractiveGuide(models.Model):
    interactive_guide = models.ForeignKey(InteractiveGuide, related_name='tooltips', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=11,
        choices=TYPE_CHOICES,
        blank=False,
    )
    page = models.CharField(max_length=255)
    target_element_id = models.CharField(max_length=255)
    target_area_element_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


# Tutorial
class TutorialStage(models.Model):
    name = models.CharField(max_length=255)
    starting_page = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class TooltipTutorial(models.Model):
    tutorial_stage = models.ForeignKey(TutorialStage, related_name='tooltips', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=11,
        choices=TYPE_CHOICES,
        blank=False,
    )
    page = models.CharField(max_length=255)
    target_element_id = models.CharField(max_length=255)
    target_area_element_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title

class TestTask(models.Model):
    tutorial = models.ForeignKey(TutorialStage, related_name='test_tasks', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.description

class ClickElement(models.Model):
    test = models.ForeignKey(TestTask, related_name='click_elements', on_delete=models.CASCADE)
    element_id = models.CharField(max_length=255)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.element_id} ({self.test})"

class TextInputElement(models.Model):
    click_element = models.ForeignKey(ClickElement, related_name='text_input_elements', on_delete=models.CASCADE)
    element_id = models.CharField(max_length=255)
    required_input = models.TextField()

    def __str__(self):
        return self.element_id
    

# Info icons
class InfoIcon(models.Model):
    target_element_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

# Documentation
class DocumentationPage(models.Model):
    page_name = models.CharField(max_length=255)
    page_id = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.page_name