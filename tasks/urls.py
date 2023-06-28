from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.ListListView.as_view(), name="tasks.index"),
    path('list/<int:list_id>', views.ItemListView.as_view(), name="tasks.list"),
]