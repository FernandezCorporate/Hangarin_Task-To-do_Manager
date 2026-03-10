from django.shortcuts import render
from django.views.generic.list import ListView
from Hangarin.models import Task
from django.db.models import F
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