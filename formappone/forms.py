from django import forms
from formappone.models import StudentDetails

class StudentDetailsForm(forms.ModelForm):
	class Meta:
		model= StudentDetails
		fields='__all__'