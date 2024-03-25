from django import forms

# Archivo donde definimos la estructura de los formularios de nuestra web

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de Tarea", max_length=200, 
                            widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripción de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))