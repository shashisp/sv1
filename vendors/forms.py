from models import Organisation
from django import forms

class OrganisationForm(forms.ModelForm):
	

	class Meta:
		model = Organisation
	
    