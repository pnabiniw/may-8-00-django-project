from django.shortcuts import render, redirect
from myapp.models import Student


def template_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        profile_picture = request.FILES.get("profile_picture")
        print(request.FILES)
        age = request.POST.get("age")
        department = request.POST.get("department")
        Student.objects.create(name=name, age=age, department=department,
                               profile_picture=profile_picture)
        return redirect('students')
    return render(request, "form/template_form.html")
