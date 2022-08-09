from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)

	@staticmethod
	def get_all_categories(self):
		return Category.objects.all()

	def __str__(self):
		self.name