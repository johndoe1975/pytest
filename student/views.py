from django.shortcuts import render
from django.views.generic import edit
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import models

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

@login_required(login_url="login/")
def list_groups(request):
	# template = loader.get_template('index.html')
	groups =  models.Group.objects.all()
	return render(request, "list_groups.html", {"groups": groups})

@login_required(login_url="login/")
def list_students(request, group_id):
	students = models.Student.objects.filter(enroled_group=group_id).all()
	return render(request, "list_student_in_group.html", {"students": students})

class StudentEditView(LoggedInMixin, edit.UpdateView):
	model = models.Student
	fields = ["full_name", "dateofbirth", "ticket_number", "enroled_group"]
	template_name = 'edit_student.html'

class GroupEditView(LoggedInMixin, edit.UpdateView):
	model = models.Group
	fields = ["name", "captain"]
	template_name = 'edit_group.html'

class StudentCreateView(LoggedInMixin, edit.CreateView):
	model = models.Student
	fields = ["full_name", "dateofbirth", "ticket_number", "enroled_group"]
	template_name = 'create_student.html'

class GroupCreateView(LoggedInMixin, edit.CreateView):
	model = models.Group
	fields = ["name", "captain"]
	template_name = 'create_group.html'

class GroupDeleteView(LoggedInMixin, edit.DeleteView):
	model = models.Group
	success_url = reverse_lazy('list_groups')
	template_name = 'delete_group.html'