from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EnrollmentForm
from .models import Course, Subject, Department, StudentProfile, Payment
from django.contrib import messages
from django.urls import reverse
from django.db import transaction

@login_required
def enroll(request):
    # if user already completed, redirect to enrollment dashboard
    if request.user.profile.enrollment_completed:
        return redirect('enrollment:dashboard')

    form = EnrollmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # save everything in a transaction
        with transaction.atomic():
            Course.objects.create(
                user=request.user,
                title=form.cleaned_data['course_title'],
                code=form.cleaned_data['course_code'],
            )
            Subject.objects.create(
                user=request.user,
                title=form.cleaned_data['subject_title'],
                code=form.cleaned_data['subject_code'],
            )
            Department.objects.create(
                user=request.user,
                name=form.cleaned_data['department_name'],
                head=form.cleaned_data['department_head'],
            )
            StudentProfile.objects.create(
                user=request.user,
                student_number=form.cleaned_data['student_number'],
                contact=form.cleaned_data['student_contact'],
            )
            Payment.objects.create(
                user=request.user,
                amount=form.cleaned_data['payment_amount'],
                reference=form.cleaned_data['payment_ref'],
            )
            # mark profile as completed
            profile = request.user.profile
            profile.enrollment_completed = True
            profile.save()
        messages.success(request, "Enrollment completed. You can now view Course/Subject/Departments/Students/Payments.")
        return redirect('navigation:dashboard')
    return render(request, 'enrollment/enroll.html', {'form': form})

@login_required
def dashboard(request):
    # show summary of user's submitted data
    courses = Course.objects.filter(user=request.user)
    subjects = Subject.objects.filter(user=request.user)
    departments = Department.objects.filter(user=request.user)
    students = StudentProfile.objects.filter(user=request.user)
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'enrollment/dashboard.html', {
        'courses': courses,
        'subjects': subjects,
        'departments': departments,
        'students': students,
        'payments': payments,
    })

# per-item views (simple list/detail could be made later)
@login_required
def course_view(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'enrollment/list.html', {'title': 'Courses', 'items': courses})

@login_required
def subject_view(request):
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'enrollment/list.html', {'title': 'Subjects', 'items': subjects})

@login_required
def departments_view(request):
    deps = Department.objects.filter(user=request.user)
    return render(request, 'enrollment/list.html', {'title': 'Departments', 'items': deps})

@login_required
def student_view(request):
    studs = StudentProfile.objects.filter(user=request.user)
    return render(request, 'enrollment/list.html', {'title': 'Students', 'items': studs})

@login_required
def payments_view(request):
    pays = Payment.objects.filter(user=request.user)
    return render(request, 'enrollment/list.html', {'title': 'Payments', 'items': pays})
