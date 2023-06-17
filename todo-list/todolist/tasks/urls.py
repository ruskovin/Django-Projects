from django.urls import path
from . import views


urlpatterns = [
    path('', views.todolist_home, name='home'),
    path('delete_task/<int:id>', views.delete_task , name='delete'),
    path('update_task/<int:id>', views.update_task, name='update'),
    path('set_status/<int:id>', views.status_update, name='set_status'),
    path('task-detail/<int:id>', views.task_detail, name='detail')
]