from django.db import models

# Create your models here.

class Task(models.Model):
    ''' This is the task model of the todo-list'''
    title = models.TextField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.title} {self.status} {self.date_created}"
    
    def __repr__(self):
        return f"{self.title} {self.status} {self.date_created}"

    def set_status(self):
        self.status = not self.status
        return

    class Meta:
        ordering = ['status','-date_created']