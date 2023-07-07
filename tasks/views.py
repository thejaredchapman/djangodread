from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from .models import TasksItem, TasksList

from django.urls import reverse


class ListListView(ListView):
    model = TasksList
    template_name = "tasks/index.html"

class ItemListView(ListView):
    model = TasksItem
    template_name = "tasks/tasks_list.html"

    def get_queryset(self):
        return TasksItem.objects.filter(tasks_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["tasks_list"] = TasksList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = TasksList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreate(CreateView):
    model = TasksItem
    fields = [
        "tasks_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        tasks_list = TasksList.objects.get(id=self.kwargs["list_id"])
        initial_data["tasks_list"] = tasks_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        tasks_list = TasksList.objects.get(id=self.kwargs["list_id"])
        context["tasks_list"] = tasks_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.tasks_list_id])

class ItemUpdate(UpdateView):
    model = TasksItem
    fields = [
        "tasks_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["tasks_list"] = self.object.tasks_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.tasks_list_id])

class ListDelete(DeleteView):
    model = TasksList
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = TasksItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_list"] = self.object.tasks_list
        return context