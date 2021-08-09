from django.urls import path
from .views import home, todoList, todoCreate, todoListCreate, todoDetail

urlpatterns = [
    path('', home),
    path('todoList/', todoList),
    path('todoCreate/', todoCreate),
    path('todoListCreate/', todoListCreate),
    path('todoDetail/<int:pk>/', todoDetail),
]
