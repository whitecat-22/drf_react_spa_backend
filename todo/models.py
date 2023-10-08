from django.db import models

class Todo(models.Model):
   name = models.CharField(max_length=64, blank=False, null=False)
   checked = models.BooleanField(default=False)

   def __str__(self):
       return self.name
