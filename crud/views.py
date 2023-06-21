from django.shortcuts import render, redirect
from myapp.models import Student, ClassRoom, StudentProfile


def home(request):
    context = {
        "title": "Home",
        "students": Student.objects.all()
    }
    return render(request, 'crud/home.html', context=context)


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


def classroom_delete(request, id):
    if request.method == "POST":
        ClassRoom.objects.filter(id=id).delete()
        return redirect("crud_classroom")
    context = {
        "classroom": ClassRoom.objects.get(id=id),
        "title": "Delete Classroom"
    }
    return render(request, "crud/classroom_delete.html", context=context)


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


def detail_student(request, id):
    context = {"title": "Student Detail", "student": Student.objects.get(id=id)}
    return render(request, 'crud/detail_student.html', context=context)


def student_delete(request, id):
    if request.method == "POST":
        Student.objects.filter(id=id).delete()
        return redirect("crud_home")
    context = {"title": "Delete Student", "student": Student.objects.get(id=id)}
    return render(request, "crud/student_delete.html", context=context)
