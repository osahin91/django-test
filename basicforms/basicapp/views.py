from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
	#renders html on index.html in basicapp folder 
	return render(request, 'basicapp/index.html')

def form_name_view(request):
	form = forms.FormName()
	if request.method == 'POST':
		form = forms.FormName(request.POST)
		if form.is_valid():
			print("Validation success!")
			print("NAME: "+ form.cleaned_data['name'])
			print("EMAIL: "+ form.cleaned_data['email'])
			print("TEXT: "+ form.cleaned_data['text'])

	return render(request, 'basicapp/form_page.html', {'form':form})