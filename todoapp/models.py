from django.db import models
from django.utils import timezone


#  Table name, has to wrap models.Model to get the functionality of Django.


class todo(models.Model):
    task_name = models.CharField(max_length=100, unique=True)# Like a VARCHAR field
    task_description = models.TextField()# Like a TEXT field
    date_created = models.DateTimeField()# Like a DATETIME field

# Tell it to return as a unicode string
# (The name of the to-do item) rather than just Object.
    def __unicode__(self):
        return self.name
