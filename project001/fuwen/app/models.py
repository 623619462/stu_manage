from django.db import models

from DjangoUeditor.models import UEditorField
class Blog(models.Model):
	name=models.CharField(max_length=100,blank=True)
	text=UEditorField()
	def __str__(self):
                return '%s is published' % (self.Name)
# Create your models here.
