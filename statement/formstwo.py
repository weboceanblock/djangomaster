from django import forms
from .models import xyz

class dataform(forms.ModelForm):
	class Meta:
		model=xyz
		fields=['credit','debit','name','date']
