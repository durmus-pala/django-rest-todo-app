from django.urls import path
from .views import home, todoListCreate, todoDetail, TodoListCreateAPIView, ToDoDetailAPIView

urlpatterns = [
    path('', home),
    # path('todoList/', todoList),
    # path('todoCreate/', todoCreate),
    # path('todoListCreate/', todoListCreate),
    path('todoListCreate/', TodoListCreateAPIView.as_view()),
    # path('todoDetail/<int:pk>/', todoDetail),
    path('todoDetail/<int:pk>/', ToDoDetailAPIView.as_view()),
]
