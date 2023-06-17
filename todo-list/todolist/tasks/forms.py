from django import forms
from tasks.models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','status')
        widgets = {
            'title': forms.TextInput(attrs={'class':'task-title ','autofocus':'true'}),
            'status': forms.CheckboxInput(attrs={'class':'task-status form-check-input bg-secondary'})
        }