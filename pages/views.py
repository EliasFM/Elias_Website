from django.shortcuts import render
from projects.models import Project

# Create your views here.
# pages/views.py

def home(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "pages/home.html", context)