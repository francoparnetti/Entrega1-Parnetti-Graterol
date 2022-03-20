from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse

from Class.models import Students
from .forms import StudentsFormulario, StudentsSearching

# Create your views here.

def forms(request):
    if request.method == 'POST':
        form = StudentsFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            students = Students(name=data['name'], last_name=data['last_name'], career=data['career'])
            students.save()
            # return render(request, "index/homepage.html", {})
            return redirect('index')

    form = StudentsFormulario()
    return render(request, "class/forms.html", {'form': form})

def students_list(request):

    name_to_search = request.GET.get('name', None)

    if name_to_search is not None:
        students = Students.objects.filter(name__icontains=name_to_search)

    else:
        students = Students.objects.all()

    form = StudentsSearching()
    return render(request, "class/students_list.html", {'form': form, 'students': students})

