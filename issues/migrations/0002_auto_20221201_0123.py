# Generated by Django 4.1.3 on 2022-12-01 01:23

from django.db import migrations

def populate_status(apps, schemaeditor):
    statuses = {
        "to do": "A task that has not yet been started",
        "in progress": "A task that is actively being worked on",
        "done": "A task that has been marked as completed"
    }
    Status = apps.get_model("issues", "Status")
    for key, value in statuses.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()

def populate_priority(apps, schemaeditor):
    priorities = {
        "low": "A low priority issue",
        "medium": "A mid-level priority issue",
        "high": "A high priority issue"
    }
    Priority = apps.get_model("issues", "Priority")
    for key, value in priorities.items():
        pr_obj = Priority(name=key, description=value)
        pr_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_status),
        migrations.RunPython(populate_priority)
    ]
