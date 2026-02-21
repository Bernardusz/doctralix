from django.db import models
from django.contrib.auth.models import User
from classroom.models import Classroom
# Create your models here.
class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=100, help_text="The full name.")
	created_at = models.DateTimeField(auto_now_add=True)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="students", related_query_name="students")
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self) -> str:
		return self.user.username