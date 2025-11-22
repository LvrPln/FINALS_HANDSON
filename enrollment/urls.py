from django.urls import path
from . import views

app_name = 'enrollment'

urlpatterns = [
    path('enroll/', views.enroll, name='enroll'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('course/', views.course_view, name='course'),
    path('subject/', views.subject_view, name='subject'),
    path('departments/', views.departments_view, name='departments'),
    path('student/', views.student_view, name='student'),
    path('payments/', views.payments_view, name='payments'),
]
