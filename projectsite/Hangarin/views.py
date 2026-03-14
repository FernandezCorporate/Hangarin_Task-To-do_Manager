from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Hangarin.models import Task, SubTask, Note
from django.db.models import F
from Hangarin.forms import TaskForm, SubTaskForm, NoteForm
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSetFactory, UpdateWithInlinesView

class DashBoardListView(ListView):
    model = Task
    template_name = "dashboard.html"
    context_object_name = "dashboard"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_tasks"] = Task.objects.count()

        completed = Task.objects.filter(
            status="Completed"
        ).count()

        context["completed"] = completed

        In_Progress = Task.objects.filter(
            status="In Progress "
        ).count()

        context["In_Progress"] = In_Progress

        Pending = Task.objects.filter(
            status="Pending"
        ).count()

        context["Pending"] = Pending

        completed_onTime = Task.objects.filter(
            status="Completed",
            updated_at__lte=F('deadline')
        ).count()

        completed_late = Task.objects.filter(
            status="Completed",
            updated_at__gt=F('deadline')
        ).count()

        if completed > 0:
            completion_rate = int((completed/context["total_tasks"]) * 100)

            if completed_onTime:
                compliancy_rate = int((completed_onTime/completed) * 100)
            else:
                compliancy_rate = 0

            if completed_late:
                deliquency_rate = int((completed_late/completed) * 100)
            else:
                deliquency_rate = 0
        else:
            completion_rate = 0


        context["Completion_rate"] = f"{completion_rate}%"
        context["Compliancy_rate"] = f"{compliancy_rate}%"
        context["Deliquency_rate"] = f"{deliquency_rate}%"

        context["model"] = "Dashboard" 

        low = Task.objects.filter(priority__name="Low").count()
        medium = Task.objects.filter(priority__name="Medium").count()
        high = Task.objects.filter(priority__name="High").count()
        optional = Task.objects.filter(priority__name="Optional").count()
        critical = Task.objects.filter(priority__name="Critical").count()

        context["low"] = low
        context["medium"] = medium
        context["high"] = high
        context["optional"] = optional
        context["critical"] = critical

        work = Task.objects.filter(category__name="Work").count()
        personal = Task.objects.filter(category__name="Personal").count()
        project = Task.objects.filter(category__name="Projects").count()
        finance = Task.objects.filter(category__name="Finance").count()
        school = Task.objects.filter(category__name="School").count()

        context["work"] = work
        context["personal"] = personal
        context["project"] = project
        context["finance"] = finance
        context["school"] = school

        return context
    
class TaskListView(ListView):
    model = Task
    template_name = 'taskList.html'
    context_object_name = 'taskList'
    paginate_by = 7

    def get_queryset(self):
        qs = super().get_queryset()
        
        query = self.request.GET.get('q')
        p_val = self.request.GET.get('priority')
        c_val = self.request.GET.get('category')
        s_val = self.request.GET.get('status')

        if query:
            qs = qs.filter(title__icontains=query)

        if p_val and p_val != "All":
            qs = qs.filter(priority__name__iexact=p_val)

        if c_val and c_val != "All":
            qs = qs.filter(category__name__iexact=c_val)

        if s_val and s_val != "All":
            qs = qs.filter(status__iexact=s_val)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["All_tasks"] = self.get_queryset().count()

        context["model"] = "Tasks"

        return context

class SubTaskInline(InlineFormSetFactory):
    model = SubTask
    form_class = SubTaskForm
    factory_kwargs = {'extra': 3, 'can_delete': False} 

class NoteInline(InlineFormSetFactory):
    model = Note
    form_class = NoteForm
    factory_kwargs = {'extra': 2, 'can_delete': False}

class SubTaskUpdateInline(InlineFormSetFactory):
    model = SubTask
    form_class = SubTaskForm
    factory_kwargs = {'extra': 0, 'can_delete': False}

class NoteUpdateInline(InlineFormSetFactory):
    model = Note
    form_class = NoteForm
    factory_kwargs = {'extra': 0, 'can_delete': False}

class TaskCreateView(CreateWithInlinesView):
    model = Task
    template_name = 'taskForm.html'
    form_class = TaskForm
    success_url = reverse_lazy('taskList')
    inlines = [SubTaskInline, NoteInline]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Add Task"
        return context

class TaskUpdateView(UpdateWithInlinesView):
    model = Task
    template_name = 'taskForm.html'
    form_class = TaskForm
    success_url = reverse_lazy('taskList')
    inlines = [SubTaskUpdateInline, NoteUpdateInline]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Update Task"
        return context

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'confirmDelete.html'
    success_url = reverse_lazy('taskList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Delete Task"
        return context

class TaskDetailListView(DetailView):
    model = Task
    template_name = 'taskDetails.html'
    context_object_name = 'taskDetails'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        completedSubTask = SubTask.objects.filter(status="Completed", parent_task_id=self.kwargs['pk']).count()
        allSubtask = SubTask.objects.filter(parent_task_id=self.kwargs['pk']).count()

        if allSubtask > 0:
            subTaskProgress = int((completedSubTask/allSubtask) * 100)
            context["progress"] = f"{subTaskProgress}%"   
        else:
                context["progress"] = "N/A"
        context["allSubtask"] = allSubtask
        context["allNote"] = Note.objects.filter(task=self.object).count()

        context["details_active"] =True
        context["model"] = "Task Details"

        
        return context

    def get_queryset(self):
        return Task.objects.prefetch_related('subtask_set', 'note_set').all()

class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtaskForm.html'

    def get_success_url(self):
        return reverse_lazy('taskDetails', kwargs={'pk': self.object.parent_task.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_task'] = Task.objects.get(id=self.kwargs['pk'])
        context["model"] = "Add SubTask"
        return context
    
class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtaskForm.html'

    def get_success_url(self):
        return reverse_lazy('taskDetails', kwargs={'pk': self.object.parent_task.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_task'] = self.object.parent_task
        context["model"] = "Update SubTask"
        return context

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'confirmDelete.html'

    def get_success_url(self):
        return reverse_lazy('taskDetails', kwargs={'pk': self.object.parent_task.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Delete SubTask"
        return context

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'noteForm.html'

    def get_success_url(self):
        return reverse_lazy('taskDetails', kwargs={'pk': self.object.task.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_task'] = Task.objects.get(id=self.kwargs['pk'])
        context["model"] = "Add Note"
        return context

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'noteForm.html'

    def get_success_url(self):
        return reverse_lazy('taskDetails', kwargs={'pk': self.object.task.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_task'] = self.object.task
        context["model"] = "Update Note"
        return context

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'confirmDelete.html'

    def get_success_url(self):
        return reverse_lazy('taskDetails', kwargs={'pk': self.object.task.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Delete note"
        return context