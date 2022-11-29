from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Issue

class BoardView(ListView):
    template_name = "issues/board.html"
    model = Issue


class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue


class IssueCreateView(CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["summary", "description", "priority", "status", "assignee"]

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)


class IssueUpdateView(UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["summary", "description", "priority", "status", "assignee"]


class IssueDeleteView(DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("board")

