from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Aquí se crean las vistas de la app con sus funciones y control de redirecciones


def index(request):
    title = 'Django Course!!!'
    # render permite recibir el request, cargar el archivo html y enviar varibles declaradas en esta función  para poder utilizarlas posteriormente en el archivo html
    return render(request, "index.html", {
        'title': title
    })


def about(request):
    username = "David"
    return render(request, "about.html", {
        'username': username
    })


def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}!!</h1>")


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all() # recoge todos los objetos pertenecientes a la clase Project que estén en la BD
    return render(request, "projects/projects.html", {
        'projects': projects
    })


def create_project(request):
    if request.method == 'GET': # SI el método lanzado es get carga la página mostrando el form
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:# Si es POST redirige a la vista completa de todos los formularios y crea el nuevo proyecto indicado en el form
        Project.objects.create(name=request.POST['name'])
        return redirect('projects') # redirect te envia al url indicado ( en este caso usamos el nombre asociado a /projects en el archivo urls.py de myapp)
    
def project_details(request, id):
    project = get_object_or_404(Project, id=id) # Si no existe un proyecto con el id indicado devuelve una 404
    tasks = Task.objects.filter(project_id = id) # Muestra aquellas tareas que estén relacionadas con el proyecto mostrado
    return render(request, 'projects/detail.html', {
      'project': project,
      'tasks': tasks
   })


def tasks(request):
    # task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


def create_task(request):
    if request.method == "GET":
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'],
                            project_id=2)
        return redirect('tasks')
