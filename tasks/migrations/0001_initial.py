# Generated by Django 4.2.1 on 2023-06-28 16:37

from django.db import migrations, models
import django.db.models.deletion
import tasks.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDoList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ToDoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("due_date", models.DateTimeField(default=tasks.models.one_week_hence)),
                (
                    "todo_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tasks.todolist"
                    ),
                ),
            ],
            options={
                "ordering": ["due_date"],
            },
        ),
    ]