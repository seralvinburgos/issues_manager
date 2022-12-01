from django.urls import path
from .views import BoardView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView


urlpatterns = [
    path('', BoardView.as_view(), name='board'),
    path('<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('new/', IssueCreateView.as_view(), name='new_issue'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='edit_issue'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='delete_issue'),
]