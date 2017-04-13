from django.db import models

# Create your models here.
class Student(models.Model):
	full_name = models.CharField(max_length=200)
	dateofbirth = models.DateField()
	ticket_number = models.IntegerField()
	enroled_group = models.ForeignKey('Group', null=True)

	def __str__(self):
		return "Student('{}', '{}', '{}')".format(self.full_name, self.dateofbirth, self.ticket_number)

	def get_absolute_url(self):
		return "/student/%i/edit" % self.id

class Group(models.Model):
	name = models.CharField(max_length=50)
	captain = models.ForeignKey(Student, null=True)

	def  __str__(self):
		return "Group('{}')".format(self.name)

	def get_absolute_url(self):
		return "/group/%i/edit" % self.id