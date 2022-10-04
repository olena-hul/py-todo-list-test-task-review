from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TagForm, TaskForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/task_list.html"
    paginate_by = 3
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = "http://127.0.0.1:8000/task/create"


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"
    paginate_by = 3


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = "http://127.0.0.1:8000/tags/create"


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class TaskChangeStatusView(View):
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()

        return redirect(reverse_lazy('todo:task-list'), permanent=True)

    def get(self, request):
        return redirect(reverse_lazy('todo:task-list'), permanent=True)
