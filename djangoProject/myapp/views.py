from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index Page</h1>")

def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}!!</h1>")

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    task = Task.objects.get(title=title)
    return HttpResponse(f'task: {task.title}')