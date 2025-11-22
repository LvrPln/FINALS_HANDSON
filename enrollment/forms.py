from django import forms

class EnrollmentForm(forms.Form):
    # course
    course_title = forms.CharField(max_length=200, label="Course Title")
    course_code = forms.CharField(max_length=50, label="Course Code")

    # subject
    subject_title = forms.CharField(max_length=200, label="Subject Title")
    subject_code = forms.CharField(max_length=50, label="Subject Code")

    # department
    department_name = forms.CharField(max_length=200, label="Department Name")
    department_head = forms.CharField(max_length=200, label="Department Head", required=False)

    # student
    student_number = forms.CharField(max_length=50, label="Student Number")
    student_contact = forms.CharField(max_length=50, label="Contact Number")

    # payment
    payment_amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount")
    payment_ref = forms.CharField(max_length=200, label="Payment Reference")
