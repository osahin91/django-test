from django import forms
from django.core import validators 

#example of custom validator. Validator checks that value starts with 'z'
def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("Must start with z")

class FormName(forms.Form):
	name = forms.CharField(validators=[check_for_z])
	email = forms.EmailField()
	verify_email = forms.EmailField(label='Enter email again')
	text = forms.CharField(widget=forms.Textarea)

	#checks if bot fills out hidden value from scraping html
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

	#checks if emails match 
	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError("Emails must match")