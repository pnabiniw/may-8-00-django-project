from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, JsonResponse
from .models import Student, ClassRoom, StudentProfile


def test(request):
    # response = HttpResponse()
    html_content = """
    <html>
    <head>
        <title>Django Project</title>
    </head>
    <body>
    <h1>Django is a web framework</h1>
    </body>
    </html>
    """
    # response.content = html_content
    return HttpResponse(html_content)


def home(request):
    return render(request, "myapp/portfolio.html")


def index(request):
    # context = {"id": 1, "name": "Arya", "age": 25, "title": "Student"}
    context = {"students": Student.objects.all(), "title": "Student"}
    # context["students"] = context["students"][:2]
    return render(request, template_name="myapp/index.html", context=context)


def view_name_jon(request):
    return render(request, template_name="myapp/jon.html")


def view_name_jane(request):
    return render(request, template_name="myapp/jane.html")


def view_name(request, name):
    last_name = request.GET.get('last_name')
    if name.lower() == 'ram':
        full_name = "Ram Bahadur"
    elif name.lower() == 'harry':
        full_name = "Harry Krishna"
    elif name.lower() == 'jon':
        full_name = "Jon Prasad"
    else:
        # return HttpResponse("<h1>Name not found</h1>", status=404)
        return HttpResponseNotFound("<h1>Name not found</h1>")
    context = {
        "name": full_name,
    }
    if last_name:
        context.update(last_name=last_name)
    return render(request, "myapp/name.html", context=context)


def json_view(request):
    response = {"id": 1, "name": "Ken", "age": 25}
    students = [
        {"id": 1, "name": "Ken", "age": 25},
        {"id": 2, "name": "Jon", "age": 22},
        {"id": 3, "name": "Arya", "age": 21},
        {"id": 4, "name": "Eren", "age": 23},
    ]
    return JsonResponse(students, safe=False)


def students(request):
    context = {
        "title": "Students",
        "classrooms": ClassRoom.objects.all(),
        "students": Student.objects.all(),
        "student_profiles": StudentProfile.objects.all()
    }
    return render(request, "myapp/students.html", context=context)


def page1(request):
    return render(request, "myapp/page1.html")


def page2(request):
    return render(request, "myapp/page2.html")


def student_detail(request, id):
    context = {
        "student": Student.objects.get(id=id),
        "title": "Student Detail"
    }
    return render(request, "myapp/student_detail.html", context=context)

# ram => Ram Bahadur
# harry =>Harry Krishna
# Jon => Jon Prasad

