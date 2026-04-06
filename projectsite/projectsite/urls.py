"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Hangarin.views import DashBoardListView, TaskListView, TaskCreateView,TaskUpdateView, TaskDeleteView, TaskDetailListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView, NoteCreateView, NoteUpdateView, NoteDeleteView, CategoryListView, PriorityListView
from Hangarin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashBoardListView.as_view(), name='dashboard'),
    path('taskList', TaskListView.as_view(), name='taskList'),
    path('taskCreate', TaskCreateView.as_view(), name='taskCreate'),
    path('taskUpdate/<int:pk>', TaskUpdateView.as_view(), name='taskUpdate'),
    path('taskDelete/<int:pk>', TaskDeleteView.as_view(), name='taskDelete'),
    path('taskDetails/<int:pk>', TaskDetailListView.as_view(), name='taskDetails'),
    path('taskDetails/<int:pk>/subtaskCreate', SubTaskCreateView.as_view(), name='subtaskCreate'),
    path('taskDetails/<int:parentTask_pk>/subtaskUpdate/<int:pk>', SubTaskUpdateView.as_view(), name='subtaskUpdate'),
    path('taskDetails/<int:parentTask_pk>/subtaskDelete/<int:pk>', SubTaskDeleteView.as_view(), name='subtaskDelete'),
    path('taskDetails/<int:pk>/noteCreate', NoteCreateView.as_view(), name='noteCreate'),
    path('taskDetails/<int:parentTask_pk>/noteUpdate/<int:pk>', NoteUpdateView.as_view(), name='noteUpdate'),
    path('taskDetails/<int:parentTask_pk>/noteDelete/<int:pk>', NoteDeleteView.as_view(), name='noteDelete'),
    path('categoryList', CategoryListView.as_view(), name='categoryList'),
    path('priorityList', PriorityListView.as_view(), name='priorityList'),
    path("accounts/", include("allauth.urls")),
    path('',include('pwa.urls')),
]
