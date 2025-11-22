from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # If enrollment not completed, redirect to enroll page
    if not request.user.profile.enrollment_completed:
        return redirect('enrollment:enroll')
    # otherwise show enrollment dashboard (summary)
    from enrollment.models import Course, Subject
    courses = Course.objects.filter(user=request.user)
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'navigation/dashboard.html', {'courses': courses, 'subjects': subjects})
