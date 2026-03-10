from django.shortcuts import render
from django.views.generic.list import ListView
from Hangarin.models import Task

class DashBoardListView(ListView):
    model = Task
    template_name = "dashboard.html"
    context_object_name = "dashboard"