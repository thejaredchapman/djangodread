from django.urls import path

from . import views

urlpatterns = [
    path("tasks", views.ListListView.as_view(), name="tasks.index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="tasks.list"),
    path("list/add/", views.ListCreate.as_view(), name="tasks.list-add"),
    path("list/<int:list_id>/item/add/", views.ItemCreate.as_view(), name="tasks.new"),
    path("list/<int:list_id>/item/<int:pk>/", views.ItemUpdate.as_view(),name="tasks.item-update"),
]