from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # Asignamos como clave foránea para las tareas la PM de Project que en este casó será el id y añadimos que si e proyecto asociado se elimina sus tareas también lo harán
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name