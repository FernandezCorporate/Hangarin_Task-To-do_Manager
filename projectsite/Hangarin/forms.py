from django.forms import ModelForm
from django import forms
from .models import Task, SubTask

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control border border-primary',
                'placeholder': 'Enter task title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control border border-primary',
                'rows': 3,
                'placeholder': 'Describe the task'
            }),

            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control border border-primary'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select border border-primary'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select border border-primary'
            }),

            'priority': forms.Select(attrs={
                'class': 'form-select border border-primary'
            }),
        }


class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control border border-primary',
                'placeholder': 'Subtask title'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select border border-primary'
            })
        }