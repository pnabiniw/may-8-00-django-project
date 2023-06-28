from django.shortcuts import render, redirect
from myapp.models import Student, ClassRoom, StudentProfile
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        "title": "Home",
        "students": Student.objects.all()
    }
    return render(request, 'crud/home.html', context=context)


@login_required
def classroom(request):
    if request.method == "POST":
        name = request.POST.get("class_name")
        ClassRoom.objects.create(name=name)
        return redirect('crud_classroom')
    context = {
        "title": "Classroom",
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, "crud/classroom.html", context=context)


@login_required
def classroom_delete(request, id):
    if request.method == "POST":
        ClassRoom.objects.filter(id=id).delete()
        return redirect("crud_classroom")
    context = {
        "classroom": ClassRoom.objects.get(id=id),
        "title": "Delete Classroom"
    }
    return render(request, "crud/classroom_delete.html", context=context)


@login_required
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        department = request.POST.get("department")
        pp = request.FILES.get("profile_picture")
        class_name = request.POST.get("classroom")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")
        class_obj = ClassRoom.objects.get(name=class_name)
        student = Student.objects.create(name=name, age=age, department=department,
                                         profile_picture=pp, classroom=class_obj)
        StudentProfile.objects.create(email=email, phone_number=phone,
                                      address=address, student=student)
        return redirect('crud_home')
    context = {
        "title": "Add Student",
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, "crud/add_student.html", context=context)


@login_required
def detail_student(request, id):
    context = {"title": "Student Detail", "student": Student.objects.get(id=id)}
    return render(request, 'crud/detail_student.html', context=context)


@login_required
def student_delete(request, id):
    if request.method == "POST":
        Student.objects.filter(id=id).delete()
        return redirect("crud_home")
    context = {"title": "Delete Student", "student": Student.objects.get(id=id)}
    return render(request, "crud/student_delete.html", context=context)


@login_required
def student_update(request, id):
    if request.method == "POST":
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")
        class_obj = ClassRoom.objects.get(name=data.pop('classroom'))
        profile_data = {}
        profile_fields = ["address", "email", "phone_number"]
        for k, v in data.items():
            if k in profile_fields:
                profile_data.update({k:v})
        data = {k:v for k, v in data.items() if k not in profile_fields}
        pp = request.FILES.get("profile_picture")
        student = Student.objects.filter(id=id)
        student.update(classroom=class_obj, **data)
        s = student[0]
        s.profile_picture = pp
        s.save()
        StudentProfile.objects.filter(student_id=id).update(**profile_data)
        return redirect('crud_home')
    context = {
        "title": "Update Student",
        "student": Student.objects.get(id=id),
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, "crud/student_update.html", context=context)
