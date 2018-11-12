from django.db import models
import datetime
# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=200)
	description =  models.CharField(max_length=300)
	due_date = models.DateField(("Date"), default=datetime.date.today)