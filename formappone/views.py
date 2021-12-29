from django.shortcuts import render
from formappone.forms import StudentDetailsForm
from formappone.models import StudentDetails

# Create your views here.
def form_display(request):
	if request.method=='GET':
		print("INSIDE GET METHOD")
		form=StudentDetailsForm()
		return render(request,'formappone/display.html',context={"form":form})

	if request.method=='POST':
		print("INSIDE POST METHOD")
		formdata=StudentDetailsForm(request.POST)


		if formdata.is_valid():
			formdata.save()


	form=StudentDetailsForm()
	return render(request,'formappone/display.html',context={"form":form})