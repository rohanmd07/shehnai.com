from django import forms
from .models import Category, Dealer, Help, Customer, Book

class create_customerForm(forms.Form):
	STATES = (
		('None', 'None'),
		('Delhi', 'Delhi'),
		('Maharashtra', 'Maharashtra'),
		('West Bengal', 'West Bengal'),
		('Rajasthan', 'Rajasthan'),
	)
	CITY = (
		('None', 'None'),
		('New Delhi', 'New Delhi'),
		('Mumbai', 'Mumbai'),
		('Kolkata', 'Kolkata'),
		('Jaipur', 'Jaipur'),
	)
	name = forms.CharField(max_length=100, widget=forms.TextInput(
			attrs={
				'class':'input100',
				'type':'text',
				'name':'name',
				'placeholder':'Name...',
				'id': 'validationTooltip01',
			}
		))
	phone = forms.CharField(widget=forms.TextInput(
			attrs={
				'class':'input100',
				'type':'text',
				'name':'phone',
				'placeholder':'phone',
				'id': 'validationTooltip02',
			}
		))
	email = forms.CharField(max_length=100, widget=forms.EmailInput(
			attrs={
				'class':'input100',
				'type':'text',
				'name':'email',
				'placeholder':'Email addess...',
				'id': 'validationTooltip03',
			}
		))	
	password = forms.CharField(max_length=100, widget=forms.PasswordInput(
			attrs={
				'class':'input100',
				'type':'text',
				'name':'pass',
				'placeholder':'*************',
				'id': 'validationTooltip04',
			}
		))	 	
	address = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'input100',
				'type':'text',
				'name':'pass',
				'placeholder': 'address',
				'id': 'validationTooltip05',
			}
		))	
	state = forms.ChoiceField(widget=forms.Select(
				attrs={
					'class': 'input100',
					'type':'text',
					'name':'pass',
					'placeholder': 'state',
					'id': 'validationTooltip06',
				}
			), choices=STATES)

	city = forms.ChoiceField(widget=forms.Select(
				attrs={
					'class': 'input100',
					'type':'text',
					'name':'pass',
					'placeholder': 'city',
					'id': 'validationTooltip07',
				}
			), choices=CITY)

class loginForm(forms.Form):
	email = forms.CharField(max_length=100, widget=forms.EmailInput(
			attrs={
				'class': 'input100',
				'placeholder': 'email',
				'id': 'validationTooltip03',
			}
		))
	password = forms.CharField(max_length=100, widget=forms.PasswordInput(
			attrs={
				'class': 'input100',
				'placeholder': 'password',
				'id': 'validationTooltip04',
			}
		))	 

class detailForm(forms.Form):
	start_date = forms.DateField(widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'type':'date',
				'placeholder': 'start date',
				'id': 'validationTooltip08',
			}
		))	 

	end_date = forms.DateField(widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'type':'date',
				'placeholder': 'end date',
				'id': 'validationTooltip09',
			}
		))	 

	marriage_date = forms.DateField(widget=forms.DateInput(
			attrs={
				'class': 'form-control',
				'type':'date',
				'placeholder': 'marriage date',
				'id': 'validationTooltip010',
			}
		))	 
