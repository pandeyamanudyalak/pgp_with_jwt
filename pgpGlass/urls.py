from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_area, name="area"),
    path('select_role',views.get_filtered_name, name="select_role"),
    path('addTask',views.addTask, name="addtask"),
    path('newTask',views.newTask, name="newTask"),
    path('oldTask',views.oldTask, name="oldTask"),
    path('closeTask',views.closeTask, name="closeTask"),
    path('completeTask',views.completeTask, name="completeTask"),
    path('notification',views.notification, name="notification"),
    path('toclose',views.toClose,name="toclose")
]