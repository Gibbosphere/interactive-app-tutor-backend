# Generated by Django 5.1.1 on 2024-09-04 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_documentation_documentationpages_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DocumentationPages',
            new_name='DocumentationPage',
        ),
    ]
