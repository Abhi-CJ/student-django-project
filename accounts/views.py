from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm,StudentForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
def login_view(request):
    return render(request, 'login.html')
def profile_view(request):
    pass

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username,password=password)
            return redirect('login')
    else:
            
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html')


def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            
            form = StudentForm()
    else:

        form = StudentForm()
    return render(request, 'accounts/student.html',{'form': form})


def view_student(request):
    query = request.GET.get('q')
    students = Student.objects.all().order_by('id')

    # SEARCH
    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query)
        )

    # PAGINATION (always)
    paginator = Paginator(students, 3)  # 3 students per page
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'accounts/view_student.html', {
        'students': students,
        'query': query
    })




def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'accounts/update_student.html', {'form': form})

def delete_student(request,id):
    student = get_object_or_404(Student,id = id)
    student.delete()
    return redirect('student_list')
    