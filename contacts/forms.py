from django import forms 
from django.core.exceptions import ValidationError 

from contacts.models import Contact , Address

class ContactForm(forms.ModelForm):

	confirm_email = forms.EmailField(
		label ="confirm email",
		required=True,
		)

	class Meta:
		model = Contact

	def __init__(self, *args, **kwargs):
			if kwargs.get('instance'):
				email=kwargs['instance'].email
				kwargs.setdefault('initial', {})['confirm_email'] = email

			return super(ContactForm, self).__init__(*args, **kwargs)	

	
	def clean(self):

		if (self.cleaned_data.get('email') != 
		   self.cleaned_data.get('confirm_email')):

		   raise ValidationError(
		   		"Email address much mactch"
		   )			

		return self.cleaned_data   



