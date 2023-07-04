from django import forms
from .models import Task, Video

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets ={
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Escribe un titulo'}),
            'description': forms.Textarea(attrs = {'class': 'form-control', 'placeholder':'Escribe una descripcion'}),
            'important': forms.CheckboxInput(attrs = {'class': 'form-check-input'}),
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video_file',)
