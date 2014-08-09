from django import forms
from models import Contact
from models import Organisation


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact

class OrganisationForm(forms.ModelForm):

	class Meta:
		model = Organisation