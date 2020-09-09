from django.urls import path
from base.views import StudentView, SingleStudentView

app_name = "base"

urlpatterns = [
    path("students/", StudentView.as_view()),
    path("students/<int:pk>", SingleStudentView.as_view())
]
